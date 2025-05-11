from utils.gen_list import *
from utils.config import Config
import os 

config = Config('config/config.json')

def restart_server(): os.system('reboot')

def download_repo(repo : str):
    domen = 'https://github.com'
    url_repo = f'{domen}/{config.git_username}/{repo}'
    for i in get_all_repo():
        base_path_repo = f'{config.git_base_dir}/{repo}'
        if i == url_repo:
            os.chdir(config.git_base_dir)
            os.system(f'git clone {url_repo}')
            os.startfile(base_path_repo)


def download_all_repo():
    for i in get_all_repo(config.git_username):
        base_path_repo = f'{config.git_base_dir}/{i.split('/')[-1]}'
        os.remove(base_path_repo)
        os.chdir(config.git_base_dir)
        os.system(f'git clone {i}')
    os.startfile(config.git_base_dir)

def systemctl(name: str, action: str):
    requests.get(f'http://{config.host}:{config.port}/{name}/{action}')

def systemctl_warpper(icon, item, service):
    action = item.text
    systemctl(service, action)
