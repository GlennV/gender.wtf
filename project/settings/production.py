from project.settings.base import *

SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = False
WSGI_APPLICATION = 'project.wsgi.production.application'

SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
CSRF_COOKIE_HTTPONLY=True
X_FRAME_OPTIONS='SAMEORIGIN'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': 'puzzle',
         'USER': 'puzzle',
         'PASSWORD': os.environ['POSTGRES_PASSWORD'],
         'HOST': 'localhost',
         'CONN_MAX_AGE': 600,
     }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'localhost:11211',
    }
}

RECAPTCHA_PUBLIC_KEY = os.environ['RECAPTCHA_PUBLIC_KEY']
RECAPTCHA_PRIVATE_KEY = os.environ['RECAPTCHA_PRIVATE_KEY']