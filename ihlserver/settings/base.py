from pathlib import Path
from datetime import timedelta
from rest_framework.settings import api_settings
from dotenv import load_dotenv
import os
import logging
import dj_database_url
import django_heroku

load_dotenv()


logging.getLogger("boto3").setLevel(logging.DEBUG)
logging.getLogger("botocore").setLevel(logging.DEBUG)
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent




SECRET_KEY = os.environ.get("SECRET_KEY")


DEBUG = True


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "django_filters",
    "rest_framework.authtoken",
    "knox",
    "storages",
    "api",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ALLOWED_HOSTS = [
    "'127.0.0.1:8000",
    "ihl-project-606adf7a8500.herokuapp.com",
    "likesgiving-two.vercel.app",
    "https://thanksgiving-two.vercel.app",
    "http://localhost:4000",
    "https://likesgiving-two.vercel.app",
]

CORS_ALLOWED_ORIGINS = [
    "https://thanksgiving-j6r1q1qck-valeriis-projects-0ac1b84e.vercel.app",
    "https://thanksgiving-two.vercel.app",
    "https://ihl-project-606adf7a8500.herokuapp.com",
    "http://localhost:4000",
    "https://likesgiving-two.vercel.app",
]

CORS_ALLOW_CREDENTIALS = True

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "knox.auth.TokenAuthentication",
    ],
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 5,
}


REST_KNOX = {
    "SECURE_HASH_ALGORITHM": "cryptography.hazmat.primitives.hashes.SHA512",
    "AUTH_TOKEN_CHARACTER_LENGTH": 64,
    "TOKEN_TTL": timedelta(
        days=90
    ),  
    "USER_SERIALIZER": "knox.serializers.UserSerializer",
    "TOKEN_LIMIT_PER_USER": None,
    "AUTO_REFRESH": True,
    "EXPIRY_DATETIME_FORMAT": "%Y-%m-%dT%H:%M:%S.%f%z",
}


ROOT_URLCONF = "ihlserver.urls"

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

WSGI_APPLICATION = "ihlserver.wsgi.application"


# Password validation


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)



STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_URLS = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# S3

S3 = True

if S3:
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_SIGNATURE_NAME = ("s3v4",)
    AWS_S3_REGION_NAME = os.environ.get("AWS_S3_REGION_NAME")
    AWS_S3_FILE_OVERWRITE = True
    AWS_DEFAULT_ACL = None
    AWS_S3_VERITY = True
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    STATICFILES_STORAGE = "storages.backends.s3boto3.S3StaticStorage"


# Email Config
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "thelikesgiving@gmail.com"
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_TIMEOUT = 300
DEFAULT_FROM_EMAIL = "theliksesgiving@gmail.com"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "api.Profile"

django_heroku.settings(locals())