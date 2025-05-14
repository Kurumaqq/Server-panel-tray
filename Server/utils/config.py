import json
from pathlib import Path

class Config():

    def __init__(self, config_path: str):
        self.config = json.load(open(config_path, 'r'))

    @property
    def port(self): return self.config['port']
    
    @property
    def base_dir_backups(self): return self.config['base_dir_backups']

    @property
    def host(self): return self.config['host']
    
    @property
    def token(self): return self.config['token']

    @property
    def services(self):
        services_path = Path('/etc/systemd/system/')
        services_list = ''
        for service in services_path.glob('*.service'):
            name = str(service).split('/')[-1]
            if name.count('.') == 1:
                services_list += f'{name.split('.')[0]};'
        return services_list[0:-1].split(';')  
