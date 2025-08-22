from eigenlib.utils.project_setup import ProjectSetup

class MainClass:
    def __init__(self):
        ProjectSetup().init()

    def launch_master(self, config):
        from eigenlib.utils.nano_net import NanoNetClass
        import time
        ################################################################################################################
        master_address = config['master_address']
        password = config['password']
        wait = config['wait']
        ################################################################################################################
        net = NanoNetClass()
        NanoNetClass.kill_processes_on_port(5005)
        net.launch_master(master_address=master_address, password=password)
        while wait:
            time.sleep(10)
        return config

    def launch_node(self, config):
        from eigenlib.utils.nano_net import NanoNetClass
        import time
        ################################################################################################################
        master_address = config['master_address']
        password = config['password']
        node_name = config['node_name']
        node_method = config['node_method']
        delay = config['delay']
        wait = config['wait']
        ################################################################################################################
        net = NanoNetClass()
        net.launch_node(node_name=node_name, node_method=node_method, master_address=master_address, password=password, delay=delay)
        while wait:
            time.sleep(10)
        return config

    def launch_client(self, config):
        from eigenlib.utils.nano_net import NanoNetClass
        ################################################################################################################
        master_address = config['master_address']
        password = config['password']
        node_name = config['node_name']
        address_node = config['address_node']
        payload = config['payload']
        delay = config['delay']
        ################################################################################################################
        net = NanoNetClass()
        net.launch_node(node_name=node_name, node_method=None, master_address=master_address, password=password, delay=delay)
        response = net.call(address_node=address_node, payload=payload)
        config['response'] = response
        net.stop()
        return config