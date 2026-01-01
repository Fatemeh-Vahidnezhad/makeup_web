from pathlib import Path
import os
import pymysql

pymysql.install_as_MySQLdb()

BASE_DIR = Path(__file__).resolve().parent.parent


def env(name, default=None):
    return os.environ.get(name, default)


def env_bool(name, default="0"):
    return str(env(name, default)).lower() in ("1", "true", "yes", "on")


# --- Security ---
SECRET_KEY = env("DJANGO_SECRET_KEY", "dev-key")   # <-- matches your PaaS variable
DEBUG = env_bool("DEBUG", "0")

# Comma-separated in PaaS:
# ALLOWED_HOSTS=celestiabeauty.ir,www.celestiabeauty.ir
ALLOWED_HOSTS = [h.strip() for h in env(
    "ALLOWED_HOSTS",
    "celestiabeauty.ir,www.celestiabeauty.ir"
).split(",") if h.strip()]

# CSRF_TRUSTED_ORIGINS=https://celestiabeauty.ir,https://www.celestiabeauty.ir
CSRF_TRUSTED_ORIGINS = [o.strip() for o in env(
    "CSRF_TRUSTED_ORIGINS",
    "https://celestiabeauty.ir,https://www.celestiabeauty.ir"
).split(",") if o.strip()]


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "products.apps.ProductsConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # If you use WhiteNoise for PaaS static files, uncomment the next line:
    # "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "makeupshop.urls"

TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [],
    "APP_DIRS": True,
    "OPTIONS": {"context_processors": [
        "django.template.context_processors.debug",
        "django.template.context_processors.request",
        "django.contrib.auth.context_processors.auth",
        "django.contrib.messages.context_processors.messages",
    ]},
}]

WSGI_APPLICATION = "makeupshop.wsgi.application"


# --- Database ---
# Preferred: use DB_* env vars (recommended)
# If you do NOT define them, it falls back to your current hard-coded values.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": env("DB_NAME", "celeir_database"),
        "USER": env("DB_USER", "celeir_ashkan"),
        "PASSWORD": env("DB_PASSWORD", "Ashkan1371_"),  # replace by env var ASAP
        "HOST": env("DB_HOST", "localhost"),
        "PORT": env("DB_PORT", "3306"),
        "OPTIONS": {"charset": "utf8mb4"},
    }
}


LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# Static/Media
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"  # best for PaaS (ephemeral). Use object storage later.

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
