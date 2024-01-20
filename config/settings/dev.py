from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-yuq%i5z!#o^d9+gx_g_@&@rc$trqm6_4fx*%d1huwbu9kyr62="


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
SERVER_ENV = "dev"

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}



# If you are using database migrations with django, setting service model migrations endpoint in here 
MIGRATION_MODULES = {
    "service_auths": f"service_auths.migrations_{SERVER_ENV}",
}
