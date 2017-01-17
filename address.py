class EnsembleAddress:
    def __init__(self, section, instrument=None, plug=None):
        self.section = section
        self.instrument = instrument
        self.plug = plug

    def __str__(self):
        return "{0}/{1}/{2}".format(self.section, self.instrument, self.plug)

    @staticmethod
    def from_string(addr_str):
        section = None
        instrument = None
        plug = None

        split = addr_str.split("/")
        if len(split) > 0:
            section = split[0]
        if len(split) > 1:
            instrument = split[1]
        if len(split) > 2:
            plug = split[2]
        return EnsembleAddress(section, instrument, plug)