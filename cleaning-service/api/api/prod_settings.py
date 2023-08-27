import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', "3.74.246.7", 'ec2-3-74-246-7.eu-central-1.compute.amazonaws.com']

DATABASES = {
    'default': {
        'ENGINE':  'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASS'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PORT': os.environ.get('DATABASE_PORT')
    }
}



# STATIC_DIR = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, "static"),
# )
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'


CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1', 'http://' + str(os.environ.get('IP_ES2'))]

