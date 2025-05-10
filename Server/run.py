from flask import Flask, request
from utils.load_rule import load_url_rule
from utils.config import Config

app = Flask(__name__)
config = Config('config/config.json')

if __name__ == '__main__':
    load_url_rule(app)
    app.run(host='0.0.0.0', port=config.port)
