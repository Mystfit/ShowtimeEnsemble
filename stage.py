""""
The stage class provides the graph state of the entire ensemble
including all available instruments, plugs and manages connections between
differen instruments and sections
"""""
import nnpy
import threading
from messages import EnsembleMessage, EnsembleUpdate
from section import Section

class Stage(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.name = "stage-poller"
        self.exit_flag = 0

        self.daemon = True
        self.sections = []
        self.query_sock = nnpy.Socket(nnpy.AF_SP, nnpy.REP)
        self.outgoing_updates = nnpy.Socket(nnpy.AF_SP, nnpy.PUB)

        self.init_network()
        self.start()

    def init_network(self):
        self.query_sock.bind("tcp://127.0.0.1:6000")
        self.outgoing_updates.bind("tcp://127.0.0.1:6001")
        self.pollset = nnpy.PollSet((self.query_sock, nnpy.POLLIN))

    def run(self):
        while not self.exit_flag:
            result = self.pollset.poll()
            for i,s in enumerate(result):
                if i == 0 and s == 1:
                    self.handle_query(EnsembleMessage.unpack(self.query_sock.recv()))

        self.join(1)

    def handle_query(self, query):
        if query.status == EnsembleUpdate.PING:
            self.query_sock.send(EnsembleMessage(EnsembleUpdate.OK).pack())
        elif query.status == EnsembleUpdate.SECTION_JOINING:
            self.sections.append(Section(query.address.section, True))
            self.query_sock.send(EnsembleMessage(EnsembleUpdate.OK).pack())
        elif query.status == EnsembleUpdate.QUERY_SECTION:
            match = None
            matching_sections = [section for section in self.sections if section.name == query.value]
            if len(matching_sections) > 0:
                match = matching_sections[0].to_dict()
            self.query_sock.send(EnsembleMessage(EnsembleUpdate.OK, None, match).pack())

    def handle_updates(self, msg):
        print("Update: " + msg)

    def close(self):
        self.exit_flag = 1
        self.query_sock.close()
        self.outgoing_updates.close()
