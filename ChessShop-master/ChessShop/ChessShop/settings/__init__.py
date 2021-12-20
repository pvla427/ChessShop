from os import environ

SERVER_MODE = environ.get('SERVER_MODE', 'LOCAL')

if SERVER_MODE == 'PRODUCTION':
    from .production import *
elif SERVER_MODE == 'LOCAL':
    from .local import *
