from pystray import Menu, MenuItem as Item
import os
from threading import Thread
from gen_list import *
from actions import *

def menu():
    return Menu(
        Item('Restart', action=lambda i, it: print('restart')),
        item_services(),
        item_reposytory(),
        item_backups(),
        Item('Config', action=lambda i, it: os.startfile('D:/dev/server_panel')),
        Item('Exit', action=lambda i, it: i.stop()),
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
        action= lambda i, it: download_repo(it.text, 'Kurumaqq', 'D:/')) 
        for i in gen_repo('Kurumaqq'))

    return Item(
            'Reposytoryes',
            Menu(
                *all_repo,
                Menu.SEPARATOR,
                Item('Download all', action=lambda i, it: print('downloads'))
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
