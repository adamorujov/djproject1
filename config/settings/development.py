from .base import *
import environ

ALLOWED_HOSTS = ['*']

DEBUG = True

AUTH_PASSWORD_VALIDATORS = [
    
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
