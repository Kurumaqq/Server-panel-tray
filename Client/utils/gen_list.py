import requests
from utils.config import Config
from bs4 import BeautifulSoup

services = []
backups = []

config = Config('config/config.json')

def get_all_repo():
    links = []
    domen = 'https://github.com'
    url = f'https://github.com/{config.git_username}?tab=repositories'
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')
    wb_break_all = soup.find_all(class_='wb-break-all')

    for i in wb_break_all:
        url_repo = f'{domen}{i.find('a').get('href')}'
        links.append(url_repo)
    return links
