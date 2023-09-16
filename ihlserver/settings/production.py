from .base import *

ALLOWED_HOSTS = ["*"]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("NAME_PG"),
        "USER": os.environ.get("USER_PG"),
        "PASSWORD": os.environ.get("PASSWORD_PG"),
        "HOST": os.environ.get("HOST_PG"),
        "PORT": os.environ.get("PORT_PG"),
    }
}
