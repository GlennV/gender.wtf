import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

PEEPL_ENVIRONMENT = ""

INTERNAL_IPS = (
    '0.0.0.0',
    '127.0.0.1',
)

ROOT_URLCONF = 'project.urls'
ASGI_APPLICATION = "project.routing.application"

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_extensions',
    'channels',
    'captcha',

    'core',
    'one',
    'three',
    'five',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'core.middleware.RedirectToNonWww',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Static files
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


LOCALE_PATHS = (
    os.path.join(BASE_DIR, "locale/"),
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets/'),
)

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
STATIC_URL = '/static/'

# Internationalization
LANGUAGE_CODE = 'en'
TIME_ZONE = 'Europe/Brussels'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Available languages
from django.utils.translation import ugettext_lazy as _

LANGUAGES = [
    ('nl', _('Nederlands')),
    ('en', _('English')),
]