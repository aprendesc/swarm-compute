
"""personal_server"""
test_config = {
    # NANO NET
    'mode': 'master',
    'master_address': 'tcp://localhost:5005',
    'password': 'test_pass',
    'node_name': 'test_node',
    'node_method': lambda a, b: a + b,
    'address_node': 'test_node',
    'payload': {'a': 1, 'b': 2},
    'delay': 1,
}
########################################################################################################################
