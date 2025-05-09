import requests
from bs4 import BeautifulSoup

services = []
backups = []


def get_all_repo(username : str):
    links = []
    domen = 'https://github.com'
    url = f'https://github.com/{username}?tab=repositories'
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')
    wb_break_all = soup.find_all(class_='wb-break-all')

    for i in wb_break_all:
        url_repo = f'{domen}{i.find('a').get('href')}'
        links.append(url_repo)
    return links
