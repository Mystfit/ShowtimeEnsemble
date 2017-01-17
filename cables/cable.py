from Queue import LifoQueue
from messages import EnsembleMessage, EnsembleUpdate

""""
Base class representing a communication channel from one plug to another
"""""
class Cable:
    def __init__(self):
        self.inbox = LifoQueue()
        self.outbox = LifoQueue()
        self.attached_plugs = {}

    def close(self):
        pass

    def attach_input(self, input_plug):
        self.attached_plugs[input_plug.address] = input_plug

    def send(self, status, address, value):
        self.outbox.put(EnsembleMessage(status, address, value))

    def recv(self, msg):
        plug = self.attached_plugs[msg.address]
        plug.recv(msg)
