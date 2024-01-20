from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "nop*15pls17hq+_e$nu+5&u9)esb_t8@8_+3pw=)djpt28+v(f"


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
SERVER_ENV = "prod"

ALLOWED_HOSTS = ["*"]


# Setting your database in production
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
