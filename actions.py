from gen_list import *
import os 

def download_repo(repo : str, username : str, base_dir):
    domen = 'https://github.com'
    url_repo = f'{domen}/{username}/{repo}'
    for i in gen_repo(username):
        if i == url_repo:
            os.chdir(base_dir)
            os.system(f'git clone {url_repo}')
            os.startfile(f'{base_dir}/{repo}')


if __name__ == "__main__":
    download_repo('tg-bot', 'Kurumaqq', 'D:/')
