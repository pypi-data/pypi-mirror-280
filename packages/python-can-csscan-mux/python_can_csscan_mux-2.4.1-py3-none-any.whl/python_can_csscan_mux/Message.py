import can
import struct

from typing import Tuple, Optional

from .Common import nob_to_dlc, dlc_to_nob


def encode_message(message: can.Message) -> bytes:
    # Allocate a buffer large enough for the header and the data. Worst case header length is 5 bytes.
    buffer = bytearray(5 + message.dlc)
    dlc = nob_to_dlc(message.dlc)
    nob = 0
    
    # Encode common header data
    buffer[0] |= (message.channel & 0x03) << 5
    buffer[0] |= 0x10 if message.is_extended_id else 0x00
    buffer[0] |= 0x08 if message.is_fd else 0x00
    buffer[0] |= dlc >> 1
    
    # Encode based on message type
    if message.is_error_frame is False:
        # Encode remainder of DLC and flags
        buffer[1] |= (dlc & 0x01) << 7
        buffer[1] |= 0x40 if message.is_rx is False else 0x00
        if message.is_fd is True:
            buffer[1] |= 0x20 if message.bitrate_switch else 0x00
        else:
            buffer[1] |= 0x20 if message.is_remote_frame else 0x00
        
        # Encode remainder of id
        if message.is_extended_id is True:
            buffer[1] |= (message.arbitration_id >> 24) & 0x1F
            buffer[2] |= (message.arbitration_id >> 16) & 0xFF
            buffer[3] |= (message.arbitration_id >> 8) & 0xFF
            buffer[4] |= message.arbitration_id & 0xFF
            
            header_bytes = 5
        else:
            buffer[1] |= (message.arbitration_id >> 8) & 0x07
            buffer[2] |= message.arbitration_id & 0xFF
            
            header_bytes = 3
        
        # Encode data
        buffer[header_bytes:header_bytes + message.dlc] = message.data[:]
        nob = header_bytes + message.dlc
    else:
        # Encode an invalid DLC value
        buffer[0] |= 0x07
        buffer[0] &= ~0x08
        
        # Encode a blank reason in the payload byte, unless there is a payload byte from the message
        if len(message.data) != 0:
            buffer[1] = message.data[0]
        else:
            buffer[1] = 0
        
        nob = 2
    
    return buffer[:nob]


def decode_message(buffer: bytes) -> Tuple[bytes, Optional[can.Message]]:
    message = can.Message()
    
    if len(buffer) == 0:
        return buffer, None
    
    # Check if regular frame or error frame
    if buffer[0] & 0x1F != 0x07:
        # Regular frame
        # Ensure there is enough data to parse the header
        if (buffer[0] & 0x10 == 0x00 and len(buffer) < 3) or (buffer[0] & 0x10 == 0x10 and len(buffer) < 5):
            # There is not enough data. Consume the entire buffer.
            return bytes(), None
        
        message.channel = (buffer[0] >> 5) & 0x07
        message.is_extended_id = (buffer[0] >> 4) & 0x01 == 0x01
        message.is_fd = (buffer[0] >> 3) & 0x01 == 0x01
        
        # Read out DLC and convert to the special value python-can uses internally
        dlc = (buffer[0] & 0x07) << 1 | (buffer[1] & 0x80) >> 7
        message.dlc = dlc_to_nob(dlc)
        
        # Ensure the DLC is valid
        if message.is_fd is False and message.dlc > 8:
            # Consume first 2 bytes of the buffer
            return buffer[2:], None
        
        message.is_rx = (buffer[1] & 0x40) != 0x40
        if message.is_fd is True:
            message.bitrate_switch = (buffer[1] & 0x20) == 0x20
        else:
            message.is_remote_frame = (buffer[1] & 0x20) == 0x20
            
        # Read the ID
        if message.is_extended_id is True:
            id, = struct.unpack_from(">I", buffer, 1)
            id &= 0x1FFFFFFF
            
            data_offset = 5
        else:
            id, = struct.unpack_from(">H", buffer, 1)
            id &= 0x7FF
            
            data_offset = 3
        
        message.arbitration_id = id
        
        if message.is_remote_frame is False:
            # Ensure there is enough data available
            if len(buffer) < data_offset + message.dlc:
                return bytes(), None
            
            message.data = buffer[data_offset:data_offset + message.dlc]
            remaining_data = buffer[data_offset + message.dlc:]
        else:
            remaining_data = buffer[data_offset:]
    else:
        # Error frame
        # Require an additional byte
        if len(buffer) < 2:
            # Consume entire buffer
            return bytes(), None
        
        message.channel = (buffer[0] >> 5) & 0x07
        message.is_error_frame = True
        message.dlc = 1
        message.data = bytes([buffer[1]])
        
        remaining_data = buffer[2:]
    
    return remaining_data, message
