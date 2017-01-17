from instrument import Instrument
from section import Section
from cable_router import CableRouter
from cables.stage_cable import StageCable


class Ensemble:
    def __init__(self, section_name, stage_host):
        self.local_section = Section(section_name)
        self.cable_router = CableRouter(stage_host)
        self.cable_router.register_section(self.local_section)

    """"
    Create a connection between two plugs
    """""
    def connect_plugs(self, out_plug, in_plug):
        pass
        # Create cable

    """"
    Create a new instrument in the local section
    """""
    def create_instrument(self, name):
        instrument = Instrument(name)
        self.local_section.add_instrument(instrument)
        return instrument

    def find_section_by_name(self, section_name):
        section_msg =  self.cable_router.query_section_by_name(section_name).value
        if section_msg:
            return Section.from_dict(section_msg)
        return None

    def close(self):
        self.cable_router.close()