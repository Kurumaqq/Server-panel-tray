import json

class Config():

    def __init__(self, config_path: str):
        self.config = json.load(open(config_path, 'r'))

    @property
    def port(self):
        return self.config['port']
    @property
    def services(self):
        return self.config['services']
    @property
    def base_dir_backups(self):
        return self.config['base_dir_backups']
    @property
    def host(self):
        return self.config['host']
