import os
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
with open(os.path.join(BASE_DIR, 'secret_key.txt')) as f:
    SECRET_KEY = f.read().strip()
# SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
# MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# Se debe activar esto en producción
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False
