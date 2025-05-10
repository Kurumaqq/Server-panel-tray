from flask import request
import os

def service_restart():
    name = request.endpoint
    os.system(f'systemctl restart {name}.service')
    return 'Успешно!!'

def service_stop():
    name = request.endpoint
    os.system(f'systemctl stop {name}.service')
    return 'Успешно!!'

def service_start():
    name = request.endpoint
    os.system(f'systemctl start {name}.service')
    return 'Успешно!!'
