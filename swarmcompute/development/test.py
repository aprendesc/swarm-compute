from eigenlib.utils.testing_utils import integrated_test_code_coverage
from eigenlib.utils.project_setup import ProjectSetupClass
ProjectSetupClass(project_folder='swarm-compute', test_environ=True)
integrated_test_code_coverage('swarmcompute')


