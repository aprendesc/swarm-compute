
apps = {
    '1':'launch_master_server',

        }
print(str(apps))
sel_n = input('Select app config: ')
sel_app = apps[sel_n]

if sel_app == 'launch_master_server':
    password = input('Set a password for the master:')
    exposed = input('Run exposed?(y/n)') == 'y'
    master_address = 'tcp://localhost:5005' if not exposed else 'tcp://95.18.166.44:5005'
    config = {
        # NANO NET
        'mode': 'master',
        'master_address': master_address,
        'password': password,
        'node_name': None,
        'node_method': None,
        'address_node': None,
        'payload': None,
        'delay': None,
    }

