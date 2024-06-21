import datetime

import can
import os
import serial
import struct

from can import Message, CanInterfaceNotImplementedError
from collections import deque
from serial.serialutil import SerialException, Timeout
from typing import Any, List, Optional, Tuple


class CSSCANSerial(can.BusABC):
    _VID_CLX000 = 0x1CBE
    _VID_CANmod = 0x04D8
    
    _PID_CLX000 = 0x021A
    _PID_CANmod = 0xEB18
    
    def __init__(self, channel: Any, can_filters: Optional[can.typechecking.CanFilters] = None, **kwargs: object):
        super().__init__(channel, can_filters, **kwargs)
        
        # Serial interface to the device
        try:
            # Open the channel with a data timeout of 1 ms
            self._channel = serial.Serial(channel, timeout=0.001)
        except SerialException:
            self._channel = None
        
        if self._channel is None:
            raise CanInterfaceNotImplementedError(f"Could not open {channel}")
        
        self.channel_info = f"CSSCAN serial on {channel}"
        
        # Event queue, contains parsed frames
        self._events = deque()
        
        # Data queue, contains raw interface data
        self._data = deque()
        
        pass
    
    def _recv_internal(self, timeout: Optional[float]) -> Tuple[Optional[Message], bool]:
        result = None
        
        t = Timeout(timeout)
        
        # Check if there are any pending events in the queue. If so, return this
        while len(self._events) == 0 and t.expired() is False:
            # Receive new data from the serial interface and pass it to the parser
            data = self._channel.read(1000000)
            self._data.extend(data)
            
            # Parse as many frames as possible
            self._parse()
        
        if len(self._events) > 0:
            result = self._events.popleft()
        
        return result, False
    
    @classmethod
    def _detect_available_configs(cls) -> List[can.typechecking.AutoDetectedConfig]:
        # Import ports based on platform, using the tools provided by pyserial
        if os.name == 'nt':
            from serial.tools.list_ports_windows import comports
        elif os.name == 'posix':
            from serial.tools.list_ports_posix import comports
        else:
            return []
        
        result = []
        ports = comports(False)
        
        for port in ports:
            # Check for VID for CLX000, CANmod
            if port.vid not in [cls._VID_CLX000, cls._VID_CANmod]:
                continue

            # Check for PID for CLX000, CANmod
            if port.pid not in [cls._PID_CLX000, cls._PID_CANmod]:
                continue
            
            current = {
                "interface": "csscan_serial",
                "channel": port.device,
            }
            
            result.append(current)
        
        return result
    
    def send(self, msg: Message, timeout: Optional[float] = None) -> None:
        payload = bytearray()
        
        # All transmission requests are ID 0x03 with flags for frame type
        tx_req = 0x03
        
        if msg.is_remote_frame is True:
            tx_req |= 0x10
        elif msg.is_fd is True:
            tx_req |= 0x20
        
        payload.append(tx_req)
        
        # Encode ID
        id = msg.arbitration_id
        if msg.is_extended_id is True:
            id |= 0x20000000
        payload.extend(struct.pack("!I", id))
        
        # Encode DLC
        payload.append(self.nob_to_dlc(len(msg.data)))
        
        # Encode data
        payload.extend(msg.data)
        
        # Calculate checksum over the data and append
        calculated_checksum = self.calculate_crc(payload)
        calculated_checksum_bytes = calculated_checksum.to_bytes(2, byteorder="big")
        payload.extend(calculated_checksum_bytes)
        
        # Stuff frame and pack in frame delimiters
        packed_frame = bytearray()
        packed_frame.append(0x7E)
        
        for i in range(len(payload)):
            if (payload[i] == 0x7D) or (payload[i] == 0x7E):
                packed_frame.append(0x7D)
                packed_frame.append(payload[i] ^ 0b00100000)
            else:
                packed_frame.append(payload[i])
        
        packed_frame.append(0x7E)
        
        self._channel.write(packed_frame)
        
        return
    
    def shutdown(self) -> None:
        super().shutdown()
        
        if self._channel is not None:
            self._channel.close()
            self._channel = None

        return
    
    def _parse(self):
        # If there are fewer bytes available than a single frame, stop parsing
        if len(self._data) < 16:
            return
        
        while len(self._data) >= 16:
            # Find start and end indices of next frame
            try:
                start_of_frame = self._data.index(0x7E, 0)
            except ValueError:
                # No start flag
                break
            
            try:
                end_of_frame = self._data.index(0x7E, start_of_frame + 1)
            except ValueError:
                # No end flag (yet)
                break

            # Skip all bytes up to the start of frame
            for _ in range(start_of_frame):
                self._data.popleft()
            
            # Extract the frame
            current_frame_raw = bytearray()
            
            for _ in range(end_of_frame - start_of_frame + 1):
                current_frame_raw.append(self._data.popleft())
            
            parsed_frame = self._parse_frame(current_frame_raw)
            if parsed_frame is not None:
                self._events.append(parsed_frame)
        
        return
    
    def _parse_frame(self, current_frame_raw):
        frame = can.Message()
        
        # Set common frame properties
        frame.is_fd = False
        frame.is_error_frame = False
        frame.bitrate_switch = False
        frame.error_state_indicator = False
        
        # Remove the start and end of frame markers
        current_frame_raw = current_frame_raw[1:-1]
        
        # Look for any stuffed bytes, and revert them
        current_frame = bytearray()
        stuff_next = False
        for i in range(len(current_frame_raw)):
            if current_frame_raw[i] == 0x7D:
                stuff_next = True
                continue
            
            current_byte = current_frame_raw[i]
            if stuff_next is True:
                current_byte ^= 0b00100000
                stuff_next = False
            else:
                current_byte = current_frame_raw[i]
            
            current_frame.append(current_byte)
        
        # Extract the checksum
        checksum = current_frame[-2:]
        current_frame = current_frame[:-2]
        calculated_checksum = self.calculate_crc(current_frame).to_bytes(2, byteorder="big")
        if checksum != calculated_checksum:
            return None
        
        # Read the frame type
        frame_type = current_frame[0]
        
        if (frame_type == 0x01) or (frame_type == 0x02) or (frame_type == 0x21) or (frame_type == 0x22):
            # Regular CAN traffic, frame either received or transmitted.
            # Extract the metadata
            seconds, milliseconds, message_id, data_length = struct.unpack_from("!IHIB", current_frame, 1)
            
            frame.timestamp = datetime.datetime.now(tz=datetime.timezone.utc).timestamp()
            frame.arbitration_id = message_id & 0x1FFFFFFF
            frame.is_extended_id = (message_id & 0x20000000) == 0x20000000
            frame.is_rx = True if frame_type == 1 else False
            frame.dlc = self.dlc_to_length(data_length)
            
            frame.is_remote_frame = (frame_type & 0x10) == 0x10
            frame.is_fd = (frame_type & 0x20) == 0x20
            
            frame.data = current_frame[12:12 + frame.dlc]
        else:
            # Unknown frame type
            pass
        
        return frame
    
    @staticmethod
    def dlc_to_length(dlc):
        length = dlc
        
        if 8 >= dlc:
            length = dlc
        elif 12 >= dlc > 8:
            length = 4 * (dlc - 9) + 12
        elif 15 >= dlc > 12:
            length = 16 * (dlc - 13) + 32
        
        return length
    
    @staticmethod
    def nob_to_dlc(nob):
        if 0 <= nob <= 8:
            return nob
        elif 8 < nob <= 12:
            return 9
        elif 12 < nob <= 16:
            return 10
        elif 16 < nob <= 20:
            return 11
        elif 20 < nob <= 24:
            return 12
        elif 24 < nob <= 32:
            return 13
        elif 32 < nob <= 48:
            return 14
        elif 48 < nob <= 64:
            return 15

    @staticmethod
    def calculate_crc(data: bytes) -> int:
        initial = 0x0000
        polynomial = 0xA001
        final = 0x0000
        
        crc = initial
        
        for b in data:
            crc ^= b
            
            for i in range(8):
                if crc & 0x0001:
                    crc >>= 1
                    crc ^= polynomial
                else:
                    crc >>= 1
        
        return crc ^ final

    pass
