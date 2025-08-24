import unittest, threading, time, copy
from eigenlib.utils.project_setup import ProjectSetup
from swarmcompute.main import MainClass
from swarmcompute.configs.base_config import Config

class TestPersonalServer(unittest.TestCase):
    def setUp(self):
        ProjectSetup().coverage()
        self.main = MainClass()
        self.delay = 5
        self.cfg = Config()

    def test_launch_master(self):
        master_cfg  = self.cfg.launch_master()
        t1 = threading.Thread(target=self.main.launch_master, args=(copy.deepcopy(master_cfg),), daemon=True)
        t1.start()
        time.sleep(self.delay)
        t1.join(timeout=0.1)

    def test_launch_node(self):
        master_cfg  = self.cfg.launch_master()
        node_cfg    = self.cfg.launch_node()
        t1 = threading.Thread(target=self.main.launch_master, args=(copy.deepcopy(master_cfg),), daemon=True)
        t2 = threading.Thread(target=self.main.launch_node, args=(copy.deepcopy(node_cfg),),   daemon=True)
        t1.start()
        t2.start()
        time.sleep(self.delay)
        t1.join(timeout=0.1)
        t2.join(timeout=0.1)

    def test_launch_client(self):
        master_cfg  = self.cfg.launch_master()
        node_cfg    = self.cfg.launch_node()
        client_cfg  = self.cfg.launch_client()
        t1 = threading.Thread(target=self.main.launch_master, args=(copy.deepcopy(master_cfg),), daemon=True)
        t2 = threading.Thread(target=self.main.launch_node, args=(copy.deepcopy(node_cfg),),   daemon=True)
        def run_client(c):
            out = self.main.launch_client(c)
            self.assertEqual(out['response'], 3)
            print('Result correct.')
        t3 = threading.Thread(target=run_client, args=(copy.deepcopy(client_cfg),), daemon=True)
        t1.start()
        t2.start()
        t3.start()
        time.sleep(self.delay)
        t1.join(timeout=0.1)
        t2.join(timeout=0.1)
        t3.join(timeout=0.1)

# DEVELOPMENT############################################################################################################
    def test_under_development(self):
        print('Development  test')