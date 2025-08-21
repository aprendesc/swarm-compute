from eigenlib.utils.databricks_serving_utils import use_endpoint
from eigenlib.utils.project_setup import ProjectSetup

class MainClass:
    def __init__(self, config):
        ProjectSetup().init()

    @use_endpoint
    def initialize(self, config):
        return config

    def launch_personal_net(self, config):
        from eigenlib.utils.nano_net import NanoNetClass
        ################################################################################################################
        mode = config['mode']
        master_address = config['master_address']
        password = config['password']
        node_name = config['node_name']
        node_method = config['node_method']
        address_node = config['address_node']
        payload = config['payload']
        delay = config['delay']
        ################################################################################################################
        net = NanoNetClass()
        if mode == 'master':
            NanoNetClass.kill_processes_on_port(5005)
            net.launch_master(master_address=master_address, password=password)
        elif mode == 'node':
            net.launch_node(node_name=node_name, node_method=node_method, master_address=master_address, password=password, delay=delay)
        elif mode == 'client':
            net.launch_node(node_name=node_name, node_method=None, master_address=master_address, password=password, delay=delay)
            response = net.call(address_node=address_node, payload=payload)
            config['response'] = response
            net.stop()
        return config

    @use_endpoint
    def project_dev_server(self, config):
        import os
        from swarmautomations.main import MainClass as SAMainClass
        config = {
            'launch_master': False,
            'node_name': os.environ['MODULE_NAME'],
            'node_delay': 1
        }
        sa_main = SAMainClass(config)
        sa_main.dev_tools_server(config)