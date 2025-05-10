from flask import Flask, request
import json
from utils.route import *
from utils.config import Config

app = Flask(__name__)

config = Config('config/config.json')

# app.add_url_rule('/tg-bot', 'tg-bot', service_restart)

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=config['port'])
    print(config.port)
    print(config.base_dir_backups)
    print(config.services)
