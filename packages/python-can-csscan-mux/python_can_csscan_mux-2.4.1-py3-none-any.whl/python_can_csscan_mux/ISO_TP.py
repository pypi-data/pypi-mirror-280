from typing import Optional

import can
import struct

from collections import deque
from enum import IntEnum

from .Common import dlc_to_nob, nob_to_dlc


class ISOTPDecoder(object):
    
    def __init__(self):
        # Data queue, contains raw interface data
        self._data = deque()
        self._iso_tp_bytes_left = 0
        self._frame_counter = 0
        
        return
    
    def parse(self, message: can.Message) -> Optional[bytes]:
        if message is None:
            return None
        elif message.dlc == 0:
            return None
        
        result = None
        
        # Look at the first byte to determine how to parse this frame
        first_byte = message.data[0]
        
        if first_byte & 0xF0 == 0x00:
            result = self._parse_single_frame(message)
        elif first_byte & 0xF0 == 0x10:
            result = self._parse_first_frame(message)
        elif first_byte & 0xF0 == 0x20:
            result = self._parse_consecutive_frame(message)
        
        return result
    
    def _parse_single_frame(self, message: can.Message) -> bytes:
        # Single frame detected, reset internal state
        self._iso_tp_bytes_left = 0
        self._frame_counter = 0
        self._data.clear()
        
        # Determine frame length
        first_byte = message.data[0]
        length = first_byte & 0x0F
        start_of_frame = 1
        
        if length == 0:
            if len(message.data) < 2:
                # Not a valid ISO-TP message
                return bytes()
            length = message.data[1]
            start_of_frame = 2
        
        # Ensure there is enough data to extract
        if len(message.data) < start_of_frame + length:
            # Not a valid ISO-TP frame
            return bytes()
        
        return message.data[start_of_frame:start_of_frame + length]
    
    def _parse_first_frame(self, message: can.Message) -> None:
        # First frame detected, reset internal state
        self._iso_tp_bytes_left = 0
        self._frame_counter = 0
        self._data.clear()
        
        # Sanity check
        if len(message.data) < 2:
            return None
        
        # Determine frame length
        length, = struct.unpack_from(">H", message.data, 0)
        length &= 0x0FFF
        
        # Append data
        self._data.extend(message.data[2:])
        
        # Update counter
        self._iso_tp_bytes_left = length - (len(message.data) - 2)
        self._frame_counter += 1
        
        return None
    
    def _parse_consecutive_frame(self, message: can.Message) -> Optional[bytes]:
        data = message.data
        
        # Ensure the frame counter matches
        frame_counter = data[0] & 0x0F
        if frame_counter != self._frame_counter:
            # Reset state
            self._data.clear()
            self._frame_counter = 0
            
            return None
        
        if (len(data) - 1) > self._iso_tp_bytes_left:
            data = data[1:1 + self._iso_tp_bytes_left]
        else:
            data = data[1:]
        
        self._data.extend(data)
        
        # Update counter
        self._iso_tp_bytes_left -= len(data)
        self._frame_counter += 1
        if self._frame_counter > 15:
            self._frame_counter = 0
        
        result = None
        
        if self._iso_tp_bytes_left == 0:
            result = bytes(self._data)
            self._data.clear()
            self._frame_counter = 0
        
        return result
    
    pass
    
    
def iso_tp_pack_frame(buffer: bytes, mtu: int) -> [can.Message]:
    packed_messages = []
    
    # Determine if the message can fit in a single ITO-TP frame, or needs to be split into multiple frames
    bytes_in_a_single_frame = mtu - 1 if mtu <= 8 else mtu - 2
    if len(buffer) <= bytes_in_a_single_frame:
        packed_messages.append(iso_tp_pack_single_frame(buffer))
    else:
        packed_messages.extend(iso_tp_pack_multi_frame(buffer, mtu))
    
    return packed_messages
    
    
def iso_tp_pack_single_frame(buffer: bytes) -> can.Message:
    header_bytes = 1 if len(buffer) <= 8 else 2
    dlc = nob_to_dlc(header_bytes + len(buffer))
    iso_tp_buffer = bytearray(dlc_to_nob(dlc))
    
    # Set up ISO-TP header
    if header_bytes == 1:
        iso_tp_buffer[0] = 0x00 | len(buffer)
    else:
        iso_tp_buffer[0] = 0x00
        iso_tp_buffer[1] = len(buffer)
    
    # Insert data
    iso_tp_buffer[header_bytes:header_bytes + len(buffer)] = buffer[:]
    
    # Insert padding if necessary
    iso_tp_buffer[header_bytes + len(buffer):] = [0xCC for _ in range(len(iso_tp_buffer) - len(buffer) - header_bytes)]
    
    # Pack into a message
    packed_msg = can.Message()
    packed_msg.dlc = len(iso_tp_buffer)
    packed_msg.data = iso_tp_buffer
    
    return packed_msg
    
    
def iso_tp_pack_multi_frame(buffer: bytes, mtu: int) -> [can.Message]:
    result = []
    
    # Need to pack the message into multiple frames. We need to transmit 2 bytes header in the first frame, and 1
    # bytes of header in all consecutive frames.
    iso_tp_buffer = bytearray(mtu)
    read_index = 0
    frame_counter = 1
    
    # Set up ISO-TP headers of the first frame
    iso_tp_buffer[0] = 0x10
    iso_tp_buffer[1] = len(buffer)
    
    # Insert data
    iso_tp_buffer[2:] = buffer[read_index:mtu - 2]
    read_index += mtu - 2
    
    # Pack into a message
    msg = can.Message()
    msg.dlc = len(iso_tp_buffer)
    msg.data = iso_tp_buffer
    result.append(msg)
    
    # Pack remaining data
    while read_index < len(buffer):
        # Reset buffer
        iso_tp_buffer = bytearray(mtu)
        
        # Pack header
        iso_tp_buffer[0] = 0x20 | frame_counter
        frame_counter += 1
        if frame_counter > 15:
            frame_counter = 0
        
        # Copy data
        bytes_to_copy = mtu - 1
        if bytes_to_copy > (len(buffer) - read_index):
            bytes_to_copy = len(buffer) - read_index
        
        iso_tp_buffer[1:1 + bytes_to_copy] = buffer[read_index:read_index + bytes_to_copy]
        read_index += bytes_to_copy
        
        if read_index == len(buffer):
            # Insert padding if necessary
            nob = dlc_to_nob(nob_to_dlc(1 + bytes_to_copy))
            iso_tp_buffer[1 + bytes_to_copy:nob] = [0xCC for _ in range(nob - (1 + bytes_to_copy))]
            bytes_to_copy += nob - (1 + bytes_to_copy)
        
        msg = can.Message()
        msg.dlc = 1 + bytes_to_copy
        msg.data = iso_tp_buffer[:1 + bytes_to_copy]
        result.append(msg)
    
    return result
