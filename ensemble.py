from instrument import Instrument
from section import Section


class Ensemble:
    def __init__(self):
        self.local_section = Section()
        self.sections = []

    """"
    Create a connection between two plugs
    """""
    def connect_plugs(self, out_plug, in_plug):
        pass
        # Create cable

    """"
    Create a new instrument in the local section
    """"
    def create_instrument(self, name):
        instrument = Instrument(name)
        self.local_section.add_instrument(instrument)
        return instrument
