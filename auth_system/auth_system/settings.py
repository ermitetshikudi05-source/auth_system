"""
Django settings for auth_system project.
"""

from pathlib import Path
import os

# ==========================
# BASE DIR
# ==========================
BASE_DIR = Path(__file__).resolve().parent.parent


# ==========================
# SECURITY
# ==========================
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-dev-key")

DEBUG = False

ALLOWED_HOSTS = [
    "auth-system-spxr.onrender.com",
    "localhost",
    "127.0.0.1",
]
CSRF_TRUSTED_ORIGINS = [
    "https://auth-system-spxr.onrender.com",
]
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


# ==========================
# APPLICATIONS
# ==========================
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "accounts",
]


# ==========================
# MIDDLEWARE
# ==========================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ==========================
# URLS / WSGI
# ==========================
ROOT_URLCONF = "auth_system.urls"
WSGI_APPLICATION = "auth_system.wsgi.application"


# ==========================
# TEMPLATES
# ==========================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# ==========================
# DATABASE
# ==========================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# ==========================
# PASSWORD VALIDATION
# ==========================
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# ==========================
# INTERNATIONALIZATION
# ==========================
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# ==========================
# STATIC FILES (WHITENOISE)
# ==========================
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# ==========================
# EMAIL - OUTLOOK SMTP (PRODUCTION)
# ==========================
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = "smtp.office365.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = os.getenv("OUTLOOK_EMAIL")
EMAIL_HOST_PASSWORD = os.getenv("OUTLOOK_PASSWORD")

DEFAULT_FROM_EMAIL = "Auth System <tshiswakaschadrack@outlook.com>"


# ==========================
# PASSWORD RESET
# ==========================
PASSWORD_RESET_TIMEOUT = 60 * 60  # 1 heure


# ==========================
# DEFAULT PRIMARY KEY
# ==========================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
