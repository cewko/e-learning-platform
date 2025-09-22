import os
from .base import *

DEBUG = False

ADMINS = [
    ("Admin", os.environ.get('ADMIN_EMAIL', "admin@domain.com")),
]

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

# Database configuration
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}