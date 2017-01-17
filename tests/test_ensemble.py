from unittest import TestCase
from ensemble import Ensemble
from stage import Stage
import time


class TestEnsemble(TestCase):
    def test_section_registration(self):
        print("Testing section registration")
        stage = Stage()
        ensemble = Ensemble("test_section", "127.0.0.1")

        test_section = ensemble.find_section_by_name("test_section")
        self.assertEqual(test_section.address.section, "test_section")

        ensemble.close()
        stage.close()


