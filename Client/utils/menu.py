from pystray import Menu, MenuItem as Item
from pathlib import Path
from utils.gen_list import *
from utils.actions import *

def menu():
    return Menu(
        Item(
            'Restart', 
             action=lambda i, it: print('restart')
        ),
        item_services(),
        item_reposytory(),
        item_backups(),
        Item(
            'Config', 
            action=lambda i, it: os.startfile(f'{Path(__file__).parent.resolve().parent.resolve()}/config')

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
    return Item(
            'Services',
            Menu(
                Item('tg-bot',
                     Menu(
                        Item('Restart',
                        action=lambda i, it: print(f'restart'),
                        ),
                        Item('Stop',
                         action=lambda i, it: print(f'stop'),
                        ),
                        Item('Start',
                         action=lambda i, it: print(f'start'),
                        ),
                    )
                ),
                Item('Discord_bot',
                     Menu(
                        Item('Restart',
                        action=lambda i, it: print(f'restart')
                        ),
                        Item('Stop',
                         action=lambda i, it: print(f'stop')
                        ),
                        Item('Start',
                         action=lambda i, it: print(f'start')
                        ),
                    )
                ),
                Item('Backups',
                     Menu(
                        Item('Restart',
                        action=lambda i, it: print(f'restart')
                        ),
                        Item('Stop',
                         action=lambda i, it: print(f'stop')
                        ),
                        Item('Start',
                         action=lambda i, it: print(f'start')
                        ),
                    )
                ),
            ),
    )
