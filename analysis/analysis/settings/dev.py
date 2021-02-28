from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

SITE_ID = 1

DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'NAME': 'analysis',
        'PASSWORD': 'analysis',
        'PORT': '',
        'USER': 'analysis'
    }
}

CURRENT_URL = 'dev'


DOMAIN = 'http://127.0.0.1:8000'
