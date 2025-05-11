from flask import request
from pathlib import Path
import os

def service_restart():
    name = request.endpoint
    os.system(f'systemctl restart {name.split('_')[0]}.service')
    return 'Успешно!!'

def service_stop():
    name = request.endpoint
    os.system(f'systemctl stop {name.split('_')[0]}.service')
    return 'Успешно!!'

def service_start():
    name = request.endpoint
    os.system(f'systemctl start {name.split('_')[0]}.service')
    return 'Успешно!!'

def get_services():
    services_path = Path('/etc/systemd/system/')
    services_list = ''
    for service in services_path.glob('*.service'):
        name = str(service).split('/')[-1]
        if name.count('.') == 1:
            services_list += f'{name.split('.')[0]};'
    return services_list[0:-1]
