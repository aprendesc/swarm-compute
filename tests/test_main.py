from swarmcompute.main import MainClass
from swarmcompute.configs.test_config import test_config as config
import unittest
import copy

class TestMainClass(unittest.TestCase):
    def setUp(self):
        self.test_delay = 5
        self.main = MainClass(config)

    def test_launch_personal_net(self):
        import threading
        import time
        ################################################################################################################
        config['mode'] = 'master'
        standby_thread_1 = threading.Thread(target=self.main.launch_personal_net, args=(copy.deepcopy(config),), daemon=True, name='1')
        standby_thread_1.start()
        config['mode'] = 'node'
        standby_thread_2 = threading.Thread(target=self.main.launch_personal_net, args=(copy.deepcopy(config),), daemon=True, name='2')
        standby_thread_2.start()
        config['mode'] = 'client'
        def aux_method(config):
            output_config = self.main.launch_personal_net(config)
            assert output_config['response'] == 3
            print(output_config['response'])
        standby_thread_3 = threading.Thread(target=aux_method, args=(copy.deepcopy(config),), daemon=True, name='3')
        standby_thread_3.start()
        time.sleep(self.test_delay)
        standby_thread_1.join(timeout=0.1)
        standby_thread_2.join(timeout=0.1)
        standby_thread_3.join(timeout=0.1)
