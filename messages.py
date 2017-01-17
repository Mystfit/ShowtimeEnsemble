from enum import Enum
import msgpack
from address import EnsembleAddress
import pickle

class EnsembleUpdate(Enum):
    SECTION_JOINING = 0
    SECTION_LEAVING = 1
    INSTRUMENT_JOINING = 2
    INSTRUMENT_LEAVING = 3
    PLUG_JOINING = 4
    PLUG_LEAVING = 5
    OK = 6
    PING = 7
    QUERY_SECTION = 8

class EnsembleMessage:
    def __init__(self, status, address=None, value=None):
        self.status = status
        self.value = value
        self.address = address

    def pack(self):
        msg = [self.status.value, str(self.address), self.value]
        return msgpack.packb(msg)

    @staticmethod
    def unpack(msg_string):
        unpacked = msgpack.unpackb(msg_string)
        status = EnsembleUpdate(unpacked[0])
        address = EnsembleAddress.from_string(unpacked[1])
        value = unpacked[2]
        return EnsembleMessage(status, address, value)