from flask import Flask
from flask_cors import CORS
from flask.logging import default_handler

app = Flask(__name__)
CORS(app)
app.config.from_pyfile('config.py')
app.logger.removeHandler(default_handler)

from picast.handlers import statusHandler, streamHandler, seekHandler, volumeHandler, controlHandler
