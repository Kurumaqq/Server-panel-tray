from utils.gen_list import *
import os 

def download_repo(repo : str, username : str, base_dir):
    domen = 'https://github.com'
    url_repo = f'{domen}/{username}/{repo}'
    for i in get_all_repo(username):
        if i == url_repo:
            os.chdir(base_dir)
            os.system(f'git clone --force {url_repo}')
            os.startfile(f'{base_dir}/{repo}')


def download_all_repo(username : str, base_dir):
    for i in get_all_repo(username):
        os.chdir(base_dir)
        os.system(f'git clone --force {i}')
    os.startfile(base_dir)
