from .base import *

SECRET_KEY = 'django-insecure-&q!6*a*9wq#bw4x=nz^^@zfue8!tk93%9z9^=kfi^9gd+br=zs'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_app_pokemon',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

STATIC_URL = 'static/'
