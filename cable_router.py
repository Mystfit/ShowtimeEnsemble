from enum import enum
from cables.nano_cable import NanoCable
import nnpy
from enum import Enum
from messages import EnsembleMessage, EnsembleUpdate
from cables.stage_cable import StageCable
from address import EnsembleAddress

class CableType(Enum):
    nano = 0
    direct = 1

class CableRouter:
    def __init__(self, stage_host):
        self.cables = {}
        self.stage_cable = StageCable(stage_host)

    def register_section(self, section):
        return self.stage_cable.query(EnsembleMessage(EnsembleUpdate.SECTION_JOINING, section.address))

    def query_section_by_name(self, section_name):
        msg = EnsembleMessage(EnsembleUpdate.QUERY_SECTION, None, section_name)
        return self.stage_cable.query(msg)

    def close(self):
        for cable in self.cables.values():
            cable.close()
        self.stage_cable.close()

    """"
    Inialize a new cable using the specified transport type
    """""
    def create_cable(self, kind):
        if kind is CableType.nano:
            return NanoCable()
        elif kind is CableType.direct:
            return DirectCable()

    def discover(self):
        self.discovery_bus = nnpy.Socket(nnpy.AF_SP, nnpy.BUS)

