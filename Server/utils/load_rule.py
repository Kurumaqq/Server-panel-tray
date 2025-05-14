from flask import Flask
from utils.config import Config
from utils.route import *

config = Config('config/config.json')

def load_url_rule(app : Flask):
    load_start_service_rule(app)
    load_restart_service_rule(app)
    load_stop_service_rule(app)
    load_get_services(app)


def load_start_service_rule(app):
    for name in config.services:
        app.add_url_rule(f'/{name}/start', f'{name}_start', service_start)

def load_restart_service_rule(app):
    for name in config.services:
        app.add_url_rule(f'/{name}/restart', f'{name}_restart', service_restart)

def load_stop_service_rule(app):
    for name in config.services:
        app.add_url_rule(f'/{name}/stop', f'{name}_stop', service_stop)

def load_get_services(app):
    app.add_url_rule('/get-services', 'get-services', get_services)

def load_send_files(app):
    app.add_url_rule('/send-file', 'send-file', files)
