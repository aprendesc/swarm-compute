

class Config:
    def __init__(self):
        self.master_address = 'tcp://0.0.0.0:5005'
        self.password = 'internal_pass'
        self.delay = 1
        self.wait = True

    def launch_master(self, update=None):
        cfg = {
            'master_address': self.master_address,
            'password': self.password,
            'wait': self.wait,
        }
        return cfg | (update or {})

    def launch_node(self, update=None):
        cfg = {
            'master_address': self.master_address,
            'password': self.password,
            'node_name': 'test_node',
            'node_method': lambda a, b: a + b,
            'delay': self.delay,
            'wait': self.wait,
        }
        return cfg | (update or {})

    def launch_client(self, update=None):
        cfg = {
            'master_address': self.master_address,
            'password': self.password,
            'node_name': 'test_client',
            'address_node': 'test_node',
            'payload': {'a': 1, 'b': 2},
            'delay': self.delay,
            'wait': self.wait,
        }
        return cfg | (update or {})