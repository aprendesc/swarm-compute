
apps = {
    '1': 'launch_master',
    '2':'launch_security_node',
    '3': 'cal_security_node',
        }
print("""
{
    '1': 'launch_master',
    '2':'launch_security_node',
    '3': 'cal_security_node',
        }
""")
sel_n = input('Select app config: ')
sel_app = apps[sel_n]

if sel_app == 'launch_master':
    password = input('Set a password for the master:')
    config = {
        # NANO NET
        'mode': 'master',
        'master_address': 'tcp://localhost:5005',
        'password': password,
        'node_name': 'security_node',
        'node_method': lambda a, b: a + b,
        'address_node': 'test_node',
        'payload': {'a': 1, 'b': 2},
        'delay': 1,
    }

elif sel_app == 'launch_security_node':
    password = input('Set a password for the security node.')
    env_file_path = input('set .env file path:')
    if input('Use localhost?(y/n):') == 'y':
        master_address = 'tcp://localhost:5005'
    else:
        master_address = 'tcp://95.18.166.44:5005'
    def aux_method(dummy_input):
        from dotenv import dotenv_values
        env_vars = dotenv_values(env_file_path)
        return env_vars
    config = {
        # NANO NET
        'mode': 'node',
        'master_address': master_address,
        'password': password,
        'node_name': 'security_node',
        'node_method': aux_method,
        'address_node': None,
        'payload': None,
        'delay': 1,
    }

elif sel_app == 'cal_security_node':
    password = input('Set a password for access.')
    config = {
        # NANO NET
        'mode': 'client',
        'master_address': 'tcp://95.18.166.44:5005',
        'password': password,
        'node_name': 'security_node',
        'node_method': None,
        'address_node': 'security_node',
        'payload': None,
        'delay': 1,
    }
