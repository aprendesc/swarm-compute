from swarmcompute.main import MainClass

class CLI:
    def __init__(self):
        print("""

██████╗░██████╗░░█████╗░░░░░░██╗███████╗░█████╗░████████╗  ░█████╗░██╗░░░░░██╗
██╔══██╗██╔══██╗██╔══██╗░░░░░██║██╔════╝██╔══██╗╚══██╔══╝  ██╔══██╗██║░░░░░██║
██████╔╝██████╔╝██║░░██║░░░░░██║█████╗░░██║░░╚═╝░░░██║░░░  ██║░░╚═╝██║░░░░░██║
██╔═══╝░██╔══██╗██║░░██║██╗░░██║██╔══╝░░██║░░██╗░░░██║░░░  ██║░░██╗██║░░░░░██║
██║░░░░░██║░░██║╚█████╔╝╚█████╔╝███████╗╚█████╔╝░░░██║░░░  ╚█████╔╝███████╗██║
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝░╚════╝░░░░╚═╝░░░  ░╚════╝░╚══════╝╚═╝
░╚════╝░╚══════╝╚═╝ 
                    """)

    def run(self):
        while True:
            print("""
========================================================================================================================
""")

            # MENU
            menu_1 = """
1- Launch Personal Server
2- Launch Security Node Setup
3- Launch Security Client

Select a method: """
            method = input(menu_1)

            # TREE
            if method == '1':
                from swarmcompute.configs.base_config import personal_server_config as config
                main = MainClass(config)
                config['mode'] = 'master'
                main.launch_personal_net(config)
            elif method == '2':
                from swarmcompute.configs.base_config import security_config as config
                main = MainClass(config)
                config['mode'] = 'node'
                main.launch_personal_net(config)
            elif method == '3':
                from swarmcompute.configs.base_config import security_config as config
                from cryptography.fernet import Fernet
                main = MainClass(config)
                config['mode'] = 'client'
                output_config = main.launch_personal_net(config)
                encrypted_vars = output_config['response']
                f = Fernet(config['payload']['public_key'])
                env_vars = {k: f.decrypt(v.encode()).decode() for k, v in encrypted_vars.items()}
                self._save_env_dict(env_vars, filepath='.env')

    def _save_env_dict(self, env_vars, filepath='.env'):
        with open(filepath, 'w') as f:
            for key, value in env_vars.items():
                f.write(f'{key}={value}\n')

if __name__ == "__main__":
    CLI().run()
