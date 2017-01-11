from cable import Cable
import nnpy
import msgpack

class NanoCable(Cable):
    def __init__(self):
        Cable.__init__(self)
        self.socket = nnpy.Socket(nnpy.AF_SP, nnpy.PAIR)

    def send(self, address, value):
        msg = {'addr':address, 'val':value}
        self.socket.send(msgpack.packb(msg))

    def recv(self):
        pass