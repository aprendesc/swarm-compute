import unittest
from eigenlib.utils.project_setup import ProjectSetupClass
from swarmcompute.main import MainClass
from swarmcompute.config import test_config as config
ProjectSetupClass(project_folder='swarm-compute', test_environ=True)

class TestMain(unittest.TestCase):
    def setUp(self):
        self.main = MainClass(config)
        self.config = config

    def test_initialize(self):
        updated_config = self.main.initialize(self.config)


if __name__ == '__main__':
    unittest.main()