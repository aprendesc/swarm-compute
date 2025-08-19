import time

from eigenlib.utils.databricks_serving_utils import use_endpoint

class MainClass:
    def __init__(self, config):
        pass

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

