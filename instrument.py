from plug import InputPlug, OutputPlug
from address import EnsembleAddress

class Instrument:
    def __init__(self, name, owner=None, locked=False):
        self.name = name
        self.owner = owner

        # Plugs
        self.inputs = []
        self.outputs = []

        # One cable per instrument link
        self.cables = []

        # If this address is a local or remote instrument
        self.locked = locked

    @staticmethod
    def from_dict(d):
        address = EnsembleAddress.from_string(d["address"])
        instrument = Instrument(address.instrument, None, True)
        return None

    def to_dict(self):
        plugs = [plug.address.to_dict() for plug in self.inputs] + [plug.address.to_dict for plug in self.ouputs]
        return {"address":str(EnsembleAddress(self.owner.name, self.name)),
                "plugs": plugs}

    def create_output_plug(self, name):
        self.outputs.append(OutputPlug(name))

    def create_input_plug(self, name):
        self.inputs.append(InputPlug(name))