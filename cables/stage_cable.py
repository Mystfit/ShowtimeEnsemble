from cable import Cable
from messages import EnsembleMessage, EnsembleUpdate
import nnpy, time

class StageCable(Cable):

    def __init__(self, stage_address):
        self.request = nnpy.Socket(nnpy.AF_SP, nnpy.REQ)
        self.request.setsockopt(nnpy.SOL_SOCKET, nnpy.RCVTIMEO, 1000)
        self.subscriber = nnpy.Socket(nnpy.AF_SP, nnpy.SUB)

        self.stage_address = stage_address
        self.request.connect("tcp://{0}:6000".format(self.stage_address))
        self.subscriber.connect("tcp://{0}:6001".format(self.stage_address))

    def close(self):
        self.request.close()
        self.subscriber.close()
        Cable.close(self)

    def ping(self):
        duration = -1
        ping_msg = EnsembleMessage(EnsembleUpdate.PING)
        start = time.time()

        response = self.query(ping_msg)
        if response:
            duration = (time.time() - start) * 1000

        return duration

    def query(self, message):
        self.request.send(message.pack())
        try:
            return EnsembleMessage.unpack(self.request.recv())
        except nnpy.NNError, e:
            print("Query timeout!")
        return None

