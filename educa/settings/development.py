from .base import *

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Development-specific settings
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Allow all hosts in development
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']