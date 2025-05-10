from flask import request
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
