from enum import enum
from nanocable import NanoCable
import nnpy

class CableType(Enum):
    nano = 0
    direct = 1

class CableRouter:
    def __init__(self):
        self.cables = {}

    """"
    Inialize a new cable using the specified transport type
    """"
    def create_cable(self, kind):
        if kind is CableType.nano:
            return NanoCable()
        elif kind is CableType.direct:
            return DirectCable()

    def discover(self):
        self.discovery_bus = nnpy.Socket(nnpy.AF_SP, nnpy.BUS)

