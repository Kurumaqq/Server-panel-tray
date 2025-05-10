from utils.gen_list import *
import os 
from shutil import rmtree, move

def download_repo(repo : str, username : str, base_dir):
    domen = 'https://github.com'
    url_repo = f'{domen}/{username}/{repo}'
    for i in get_all_repo(username):
        base_path_repo = f'{base_dir}/{repo}'
        if i == url_repo:
            os.chdir(base_dir)
            move(f'{base_path_repo}/.git', f'{base_path_repo}/tmp)')
            os.system(f'git clone {url_repo}')
            os.startfile(base_path_repo)


def download_all_repo(username : str, base_dir):
    for i in get_all_repo(username):
        base_path_repo = f'{base_dir}/{i.split('/')[-1]}'
        os.remove(base_path_repo)
        os.chdir(base_dir)
        os.system(f'git clone {i}')
    os.startfile(base_dir)
