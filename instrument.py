from plug import InputPlug, OutputPlug

class Instrument:
    def __init__(self, name, local=True):
        self.name = name

        # Plugs
        self.inputs = []
        self.outputs = []

        # One cable per instrument link
        self.cables = []

        # If this address is a local or remote instrument
        self.is_local = local

    def create_output_plug(self, name):
        self.outputs.append(OutputPlug(name))

    def create_input_plug(self, name):
        self.inputs.append(InputPlug(name))