from address import EnsembleAddress

class Plug:
    def __init__(self, name, owner=None):
        self.name = name
        self.cable = None
        self.address = None
        self.owner = owner
        self.attached_plugs = []

    def connect(self, cable):
        self.cable = cable

    @staticmethod
    def from_dict(d):
        addr = EnsembleAddress.from_string(d["address"])
        plug = Plug(addr.plug)

    def to_dict(self):
        return {"address":str(EnsembleAddress(self.owner.owner.name, self.owner.name, self.name)),
                "attachedplugs": [str(addr) for addr in self.attached_plugs]}

class InputPlug(Plug):
    def recv(self, msg):
        print(msg)

class OutputPlug(Plug):
    def send(self, value):
        self.cable.send(self.address, value)

