

class Config:
    def __init__(self, master_address='tcp://localhost:5005', password='internal_pass', delay=1, wait=True):
        self.master_address = master_address
        self.password = password
        self.delay = delay
        self.wait = wait

    def launch_master(self, update=None):
        cfg = {
            'master_address': self.master_address,
            'password': self.password,
            'wait': self.wait,
        }
        return cfg | (update or {})

    def launch_node(self, node_name='test_node', node_method=lambda a, b: a + b, payload=None, update=None):
        cfg = {
            'master_address': self.master_address,
            'password': self.password,
            'node_name': node_name,
            'node_method': node_method,
            'address_node': node_name,
            'payload': payload or {'a': 1, 'b': 2},
            'delay': self.delay,
            'wait': self.wait,
        }
        return cfg | (update or {})

    def launch_client(self, address_node='test_node', payload=None, node_name='client_node', update=None):
        cfg = {
            'master_address': self.master_address,
            'password': self.password,
            'node_name': node_name,
            'node_method': None,
            'address_node': address_node,
            'payload': payload or {'a': 1, 'b': 2},
            'delay': self.delay,
            'wait': self.wait,
        }
        return cfg | (update or {})