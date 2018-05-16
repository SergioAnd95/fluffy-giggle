import logging

HOST = '127.0.0.1'
PORT = 8000

logger = logging.getLogger('app')
logger.setLevel(logging.DEBUG)
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
logger.addHandler(console)

DATABASE = {
    'database': 'fluffy',
    'password': 'fluffy',
    'user': 'fluffy',
    'host': 'localhost'
}

REDIS = 'localhost', 6379