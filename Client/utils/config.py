import json

class Config():
    def __init__(self, config_path: str):
        self.config = json.load(open(config_path, 'r'))

    @property
    def git_username(self):
        return self.config['git_username']
    
    @property
    def git_base_dir(self):
        return self.config['git_base_dir']

    @property
    def backups_base_dir(self):
        return self.config['backups_base_dir']
    
    @property
    def sevices(self):
        return self.config['sevices']
