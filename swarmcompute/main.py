from eigenlib.utils.databricks_serving_utils import use_endpoint
from eigenlib.utils.project_setup import ProjectSetupClass
ProjectSetupClass(project_folder='swarm-compute')

class MainClass:
    def __init__(self, config={}):
        self.hypothesis = config['hypothesis']
        self.use_cloud = config['use_cloud']
        self.use_wandb = config['use_wandb']

    @use_endpoint
    def initialize(self, config):
        return config

if __name__ == '__main__':
    from swarmcompute.config import code_assistant_config as config
    main = MainClass(config)
    #main.initialize(config)
    #main.tools_setup(config)
    #main.dataset_generation(config)
    #main.dataset_labeling(config)
    #main.train(config)
    #main.eval(config)
    #main.predict(config)
    #main.telegram_chatbot_run(config)
    main.launch_front(config)