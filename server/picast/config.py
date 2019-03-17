import os

HOST = os.environ.get('HOST', '0.0.0.0')
PORT = os.environ.get('PORT', '8000')
LOG_PATH = os.environ.get('LOG_PATH', 'picast.log')
LOG_BASE = 'logbase.cfg'
