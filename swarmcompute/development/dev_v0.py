import unittest
from eigenlib.utils.project_setup import ProjectSetup
from swarmcompute.main import Main
from swarmcompute.configs.base_config import Config

class TestDev(unittest.TestCase):
    def setUp(self):
        ProjectSetup().coverage()
        self.main = Main()
        self.cfg = Config()

    def test_under_development(self):
        print('Development  test')