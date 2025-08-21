
apps = {
    '1':'launch_master_server',
        }
print(str(apps))
sel_n = input('Select app config: ')
sel_app = apps[sel_n]

if sel_app == 'launch_master_server':
    password = input('Set a password for the master:')
    config = {
        # NANO NET
        'mode': 'master',
        'master_address': 'tcp://localhost:5005',
        'password': password,
        'node_name': None,
        'node_method': None,
        'address_node': None,
        'payload': None,
        'delay': None,
    }

