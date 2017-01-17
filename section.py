from address import EnsembleAddress

class Section:
    def __init__(self, name, locked=False):
        self.name = name
        self.instruments = []
        self.locked = locked
        self.address = EnsembleAddress(self.name)

    def add_instrument(self, instrument):
        self.instruments.append(instrument)

    @staticmethod
    def from_dict(d):
        address = EnsembleAddress.from_string(d["address"])
        section = Section(address.section, True)
        return section

    def to_dict(self):
        return {"address": str(self.address), "instruments": [ins.to_dict() for ins in self.instruments]}


