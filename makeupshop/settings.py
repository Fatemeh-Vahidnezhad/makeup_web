from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'dev-key'
DEBUG = False
ALLOWED_HOSTS = ["celestiabeauty.ir", "www.celestiabeauty.ir"]
CSRF_TRUSTED_ORIGINS = ["https://celestiabeauty.ir", "https://www.celestiabeauty.ir"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'products.apps.ProductsConfig',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware','django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware','django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware','django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'makeupshop.urls'

TEMPLATES = [{
        'BACKEND':'django.template.backends.django.DjangoTemplates',
        'DIRS':[],
        'APP_DIRS':True,
        'OPTIONS':{'context_processors':[
            'django.template.context_processors.debug','django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth','django.contrib.messages.context_processors.messages',
        ],},
}]

WSGI_APPLICATION = 'makeupshop.wsgi.application'

DATABASES = {
  "default": {
    "ENGINE": "django.db.backends.mysql",
    "NAME": "celeir_database",
    "USER": "celeir_ashkan",
    "PASSWORD": "Ashkan1371_",
    "HOST": "localhost",
    "PORT": "3306",
    "OPTIONS": {"charset": "utf8mb4"},
  }
}


LANGUAGE_CODE='en-us'
TIME_ZONE='UTC'
USE_I18N=True
USE_TZ=True

STATIC_URL = "/static/"
STATIC_ROOT = "/home/celeir/apps/makeup_web/staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = "/home/celeir/public_html/media"

DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'
