from flask import Flask
from .config import Config
from .route import *

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
