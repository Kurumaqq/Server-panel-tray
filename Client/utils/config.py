import json
import requests

class Config():
    def __init__(self, config_path: str):
        self.config = json.load(open(config_path, 'r'))

    @property
    def host(self): return self.config['host']

    @property
    def port(self): return self.config['port']
    
    @property
    def git_username(self): return self.config['git_username']
    
    @property
    def git_base_dir(self): return self.config['git_base_dir']

    @property
    def backups_base_dir(self): return self.config['backups_base_dir']
    
    @property
    def token(self): return self.config['token']

    @property
    def ignored_services(self): return self.config['ignored_services']

    @property
    def sevices(self):
        services = requests.get(
            f'http://{self.host}:{self.port}/get-services',
            headers={'Authorization': self.token},
            ).text
    
        return services.split(';')
