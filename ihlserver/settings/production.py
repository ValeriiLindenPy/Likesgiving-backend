from .base import *

# TODO: I would be specific about the dns allowed here
# TODO: I would put DEBUG=False in production to prevent hackers to find potential breaches in the debugging window
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
