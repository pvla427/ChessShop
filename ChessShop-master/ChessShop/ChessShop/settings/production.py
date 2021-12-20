from .base import *

DEBUG = False

INSTALLED_APPS += [
    'corsheaders'
]

MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': environ.get('DB_NAME', ''),
        'USER': environ.get('DB_USER', ''),
        'PASSWORD': environ.get('DB_PASSWORD', ''),
        'HOST': environ.get('DB_HOST', ''),
        'PORT': environ.get('DB_PORT', '5432'),
    }
}
# HOST CONFIGURATION
SETTLEMENT_HOST = environ.get('SETTLEMENT_HOST', '127.0.0.1')
ALLOWED_HOSTS = [SETTLEMENT_HOST]

CORS_ALLOW_ALL_ORIGINS = True

STATIC_ROOT = environ.get('STATIC_ROOT','')