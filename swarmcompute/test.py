import unittest
from eigenlib.utils.project_setup import ProjectSetupClass
ProjectSetupClass(project_folder='swarm-compute', test_environ=True)

########################################################################################################################
"""SWARM AUTOMATIONS TESTS"""
########################################################################################################################

class UnitTestMainClass(unittest.TestCase):
    def setUp(self):
        from eigenlib.utils.testing_utils import TestingUtilsClass
        from swarmcompute.main import MainClass
        ################################################################################################################
        ################################################################################################################
        self.test_df, self.model, self.image, self.texto = TestingUtilsClass().get_dummy_data()
        self.main = MainClass({})

class UnitTestModulesClass(unittest.TestCase):
    def setUp(self):
        import os
        from eigenlib.utils.testing_utils import TestingUtilsClass, module_test_coverage
        ################################################################################################################
        module_test_coverage(os.environ['PROJECT_NAME'] + '.modules', self)
        self.test_df, self.model, self.image, self.texto = TestingUtilsClass().get_dummy_data()

