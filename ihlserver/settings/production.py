from .base import *

ALLOWED_HOSTS = ["ihl-project-606adf7a8500.herokuapp.com"]


# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": os.environ.get("NAME_PG"),
#         "USER": os.environ.get("USER_PG"),
#         "PASSWORD": os.environ.get("PASSWORD_PG"),
#         "HOST": os.environ.get("HOST_PG"),
#         "PORT": os.environ.get("PORT_PG"),
#     }
# }


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

