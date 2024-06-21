import can
import copy
import io

from can import Message, CanInterfaceNotImplementedError
from collections import deque
from time import sleep
from typing import Any, Dict, Optional, Tuple, Union, List

from .ISO_TP import iso_tp_pack_frame, ISOTPDecoder
from .Message import decode_message, encode_message
from .Timeout import Timeout


class CSSCANMux(can.BusABC):
    
    def __init__(self, channel: Any, can_filters: Optional[can.typechecking.CanFilters] = None, **kwargs: object):
        super().__init__(channel, can_filters, **kwargs)
        
        # We need an underlying bus to feed data. If the channel is not such an instance, check for additional
        # arguments to instantiate a driver.
        if not isinstance(channel, can.BusABC):
            # Not a bus instance, attempt to instantiate a driver with this resource instead
            interface = kwargs.get("driver", "csscan_serial")
            
            self._wrapped = can.Bus(channel=channel, interface=interface, **kwargs)
        else:
            self._wrapped = channel
        
        if self._wrapped is None:
            raise CanInterfaceNotImplementedError(f"Could not open {channel}")
        
        self.channel_info = f"CSSCAN mux on {channel}"
        
        # Parse muxing information
        raw_mux_input = kwargs.get("mux_input", "010:1;2;3;4")
        mux_input = self._parse_config(raw_mux_input)
        
        self._input_config = mux_input
        
        raw_mux_output = kwargs.get("mux_output", "011:1;2;3;4")
        mux_output = self._parse_config(raw_mux_output)
        
        # Flip the dictionary
        self._output_config = {}
        for key, values in mux_output.items():
            for i, value in enumerate(values):
                if value == "":
                    continue
                self._output_config[value] = (key, i)
                
        # Ensure that the requested channel is not part of the lists
        comparison = str(channel)
        for values in [*mux_input.values(), *mux_output.values()]:
            for value in values:
                if comparison == value:
                    raise ValueError(f"Channel {comparison} is part of the mapping")
        
        # Determine output format
        self._use_fd = kwargs.get("mux_fd", True)
        self._use_brs = kwargs.get("mux_brs", self._use_fd)
        
        # Sanity check. If the underlying channel does not support FD/BRS and they are enabled, throw an error
        if self._use_brs is True and self._use_fd is False:
            raise ValueError("BRS enabled but FD is disabled")
        
        # NOTE: I would like to enable the following check, but it doesn't work with virtual busses
#        if self._use_fd is True and self._wrapped.protocol == can.CanProtocol.CAN_20:
#            raise ValueError("FD enabled but underlying channel does not support it")
        
        # Event queue, contains parsed frames
        self._events = deque()
        
        # ISO-TP decoder
        self._iso_tp = ISOTPDecoder()
        
        return
    
    @staticmethod
    def _parse_config(config: Union[str, Dict]) -> Dict:
        result = {}
        
        if isinstance(config, dict):
            result = config
        elif isinstance(config, str):
            split_configs = config.split(",")
            
            for split_config in split_configs:
                # Extract ID to map and channel configuration
                parts = split_config.split(":")
                
                if len(parts) != 2:
                    raise ValueError(f"Expected two parts, but got {len(parts)}")
                
                id = int(parts[0], 16)
                if len(parts[0]) == 8:
                    id |= 0x80000000
                channels = parts[1].split(";")
                
                for i, channel in enumerate(channels):  # type: int, str
                    if id not in result.keys():
                        result[id] = []
                    result[id].append(channel)
        else:
            raise TypeError(f"Unexpected config type: {type(config)}")
        
        return result
    
    def _recv_internal(self, timeout: Optional[float]) -> Tuple[Optional[Message], bool]:
        result = None
        
        t = Timeout(timeout)
        
        # Check if there are any pending events in the queue. If so, return this
        while len(self._events) == 0 and t.expired() is False:
            # Receive new data from the serial interface and pass it to the parser
            message = self._wrapped.recv(timeout=t.time_left())
            
            if message is None:
                continue
            
            # If the message ID is in the internal mapping dictionary, continue parsing the frame. Else, emit it
            # directly.
            message_id = message.arbitration_id
            if message.is_extended_id is True:
                message_id |= 0x80000000
            
            if message_id in self._input_config.keys():
                # De-wrap ISO-TP
                data = self._iso_tp.parse(message)
                
                if data is not None:
                    self._parse_frames(data, message_id, message.timestamp)
            else:
                # Emit directly
                self._events.append(message)
        
        if len(self._events) > 0:
            result = self._events.popleft()
        
        return result, False
    
    def send(self, msg: Message, timeout: Optional[float] = None) -> None:
        # Look up the ID to send this message on
        tx_id = self._output_config.get(str(msg.channel), None)
        
        if tx_id is None:
            # No configured ID for this channel, forward the raw message
            self._wrapped.send(msg, timeout)
            return
        
        # Correct the value in a cloned message, to avoid changing the parameter value
        msg_to_encode = copy.deepcopy(msg)
        msg_to_encode.channel = tx_id[1]
        
        # Encode the cloned message
        encoded_message = encode_message(msg_to_encode)
        
        # Encode using ISO-TP
        mtu = 64 if self._use_fd else 8
        packed_messages = iso_tp_pack_frame(encoded_message, mtu)
        
        # Set common options
        for packed_message in packed_messages:
            packed_message.is_fd = self._use_fd
            packed_message.bitrate_switch = self._use_brs
            packed_message.arbitration_id = tx_id[0] & 0x1FFFFFFF
            packed_message.is_extended_id = (tx_id[0] & 0x80000000) == 0x80000000
        
        # Send using the wrapped connection
        for packed_message in packed_messages:
            self._wrapped.send(packed_message, timeout=timeout)
            
            if len(packed_messages) > 1:
                # This seems to be required for socketcan
                sleep(0.001)
        
        return
    
    def shutdown(self) -> None:
        super().shutdown()
        
        self._wrapped.shutdown()
        
        return
    
    def _parse_frames(self, data: bytes, config_id: int, timestamp: float) -> None:
        current_timestamp = timestamp
        
        while len(data) > 0:
            # Extract single frame from the data stream
            remaining_data, message = decode_message(data)
            
            # Truncate data
            data = remaining_data
            
            if message is None:
                continue
            
            # Look up frame mapping in config
            mapping_config = self._input_config.get(config_id, None)
            mapped_channel = None
            
            if mapping_config is not None:
                mapped_channel = mapping_config[message.channel]
                if len(mapped_channel) == 0:
                    # Channel not mapped
                    continue
            
            message.channel = mapped_channel
            
            # Handle timestamp
            message.timestamp = current_timestamp
            current_timestamp += 0.000000001
            
            self._events.append(message)
        
        return
    
    @staticmethod
    def decode(messages: List[can.Message]) -> List[can.Message]:
        result = []
        
        # Create a temporary ISO-TP decoder
        iso_tp_decoder = ISOTPDecoder()
        
        for message in messages:
            # Feed data through ISO-TP decoder
            data = iso_tp_decoder.parse(message)
            
            if data is None:
                continue
            
            timestamp = message.timestamp
            while len(data) > 0:
                # Feed data through frame parser
                data, frame = decode_message(data)
                
                if frame is None:
                    continue
                
                # Preserve timestamp
                frame.timestamp = timestamp
                timestamp += 0.000000001
                result.append(frame)
        
        return result
    
    @staticmethod
    def encode(messages: List[can.Message], mtu: int) -> List[can.Message]:
        buffer = io.BytesIO()
        
        for message in messages:
            if not isinstance(message.channel, int):
                raise ValueError(f"Channel is not an integer for {message.channel}")
            
            # Encode message
            encoded_data = encode_message(message)
            buffer.write(encoded_data)
        
        # Pack into ISO-TP
        result = iso_tp_pack_frame(buffer.getvalue(), mtu)
        
        return result
    
    pass
