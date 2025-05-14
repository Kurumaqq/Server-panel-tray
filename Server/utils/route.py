from flask import request
from flask import send_file
from utils.config import Config
from pathlib import Path
import os

config = Config('config/config.json')

def service_restart():
    name = request.endpoint
    token = request.headers.get('Authorization')
    if token == config.token:
        os.system(f'systemctl restart {name.split('_')[0]}.service')
        return '200'
    return '401'

def service_stop():
    name = request.endpoint
    token = request.headers.get('Authorization')
    print(token)
    print(config.token)
    if token == config.token:
        os.system(f'systemctl stop {name.split('_')[0]}.service')
        return '200'
    return '401'

def service_start():
    name = request.endpoint
    token = request.headers.get('Authorization')
    if token == config.token:
        os.system(f'systemctl start {name.split('_')[0]}.service')
        return 'Успешно!!'
    return '401'

def get_services():
    token = request.headers.get('Authorization')
    if token == config.token:
        services_path = Path('/etc/systemd/system/')
        services_list = ''
        for service in services_path.glob('*.service'):
            name = str(service).split('/')[-1]
            if name.count('.') == 1:
                services_list += f'{name.split('.')[0]};'
        return services_list[0:-1]
    return '401'

def files():
    token = request.headers.get('Authorization')
    if token == config.token:
        a = 'D:/test/database.zip'
        return send_file(
            a, 
            as_attachment=True,
            download_name=a.split('/')[-1]
            )
    return '401'
