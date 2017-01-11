from Queue import LifoQueue

""""
Base class representing a communication channel from one plug to another
"""""
class Cable:
    def __init__(self, internal=False):
        self.internal = internal
        self.inbox = LifoQueue()
        self.outbox = LifoQueue()
        self.attached_plugs = {}

    def attach_input(self, input_plug):
        self.attached_plugs[input_plug.address] = input_plug

    def send(self, address, value):
        self.outbox.put(CableMsg(address, value))

    def recv(self, msg):
        plug = self.attached_plugs[msg.address]
        plug.recv(msg)

class CableMsg:
    def __init__(self, address, value):
        self.address = address
        self.value = value