from pystray import Menu, MenuItem as Item
from pathlib import Path
from functools import partial
from utils.config import Config
from utils.gen_list import *
from utils.actions import *

config = Config('config/config.json')

def menu():
    return Menu(
        item_services(),
        item_reposytory(),
        item_backups(),
        Item(
            'Config', 
            action=lambda i, it: os.startfile(f'{Path(__file__).parent.resolve().parent.resolve()}/config')

        ),
        Item(
            'Restart', 
             action=lambda i, it: restart_server()
        ),
        Menu.SEPARATOR,
        Item(
            'Restart', 
            action=lambda i, it: i.stop()
        ),
        Item(
            'Exit', 
            action=lambda i, it: i.stop()
        ),
    )

def item_backups():
    return Item(
        'Backups',
            Menu(
                Item('Backup1', action=lambda i, it: print(f'download {it.text}')),
                Item('Backup1', action=lambda i, it: print(f'download {it.text}')),
                Menu.SEPARATOR,
                Item('Download all', action=lambda i, it: print('downloads'))
            )
    )

def item_reposytory():
    all_repo = (
        Item(i.split('/')[-1], 
        action= lambda i, it: download_repo(it.text, 'Kurumaqq', r'D:\Repo')) 
        for i in get_all_repo('Kurumaqq'))

    return Item(
            'Reposytoryes',
            Menu(
                *all_repo,
                Menu.SEPARATOR,
                Item('Download all', 
                     action=lambda i, it: download_all_repo('Kurumaqq', r'D:\Repo'))
            )
        )

def item_services():
    services = config.sevices
    action_list = ['start', 'stop', 'restart']
    menu_items = []
    submenu_items = []
    
    for service in services: 
        if service in config.ignored_services:
            continue
        
        for action in action_list:
            submenu_items.append(Item(
                action, 
                partial(systemctl_warpper, service=service)
                )
            )
        menu_items.append(Item(service, Menu(*submenu_items)))
        submenu_items = []

    return Item('Services',Menu(*menu_items))
