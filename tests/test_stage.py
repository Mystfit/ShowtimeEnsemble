from unittest import TestCase
from stage import Stage
from cables.stage_cable import StageCable
from messages import EnsembleMessage, EnsembleUpdate
import nnpy, time
from ensemble import Ensemble

class TestStage(TestCase):
    def test_ping(self):
        print("Testing stage ping timeout")
        stage_cable = StageCable("127.0.0.1")
        self.assertIs(stage_cable.ping(), -1)

        print("Testing stage ping")
        stage = Stage()
        time.sleep(1)
        self.assertGreaterEqual(stage_cable.ping(), 0)

        stage.close()
        stage_cable.close()






