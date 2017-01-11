class Plug:
    def __init__(self, name, owner):
        self.name = name
        self.cable = None
        self.address = None
        self.owner = owner

    def connect(self, cable):
        self.cable = cable


class InputPlug(Plug):
    def recv(self, msg):
        print(msg)


class OutputPlug(Plug):
    def send(self, value):
        self.cable.send(self.address, value)


