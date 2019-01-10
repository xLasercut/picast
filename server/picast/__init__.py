import logging
from flask import Flask
from flask_cors import CORS
from flask.logging import default_handler


app = Flask(__name__)
CORS(app)
app.config.from_pyfile("config.cfg")
from picast.handlers import statusHandler

app.logger.removeHandler(default_handler)

logPath = app.config["LOG_PATH"]
logFormat = "%(asctime)s | PiCast Service | %(levelname)s | %(message)s"
formatter = logging.Formatter(logFormat)


fileHandler = logging.FileHandler(logPath)
fileHandler.setFormatter(formatter)
app.logger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(formatter)
app.logger.addHandler(consoleHandler)

app.logger.setLevel(logging.DEBUG)
