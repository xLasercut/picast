from flask import Flask
from flask_cors import CORS
from flask.logging import default_handler

app = Flask(__name__)
CORS(app)
app.config.from_pyfile('config.cfg')
app.logger.removeHandler(default_handler)

from picast.logging import LogObject

from picast.handlers import statusHandler, streamHandler, seekHandler, volumeHandler, controlHandler
