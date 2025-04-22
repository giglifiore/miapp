from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'clave-secreta-fake-para-desarrollo'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'home',
    'app',
]

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'miapp.urls'

TEMPLATES = []

WSGI_APPLICATION = 'miapp.wsgi.application'

STATIC_URL = '/static/'
