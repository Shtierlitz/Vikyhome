import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    "3.74.141.58",
    'ip-172-31-42-188.eu-central-1.compute.internal',
    'vikyhome.com.ua',
    'www.vikyhome.com.ua'
]

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
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'


CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1',
    f"http://{str(os.environ.get('IP_ES2'))}",
    'https://vikyhome.com.ua',
    'https://www.vikyhome.com.ua'
]


