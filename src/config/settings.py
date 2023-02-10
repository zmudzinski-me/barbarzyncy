import os

from django.utils.translation import gettext_lazy as _

import environ
from dotenv import load_dotenv


env = environ.Env()
root = environ.Path(__file__) - 2
load_dotenv()

BASE_DIR = root()
DEBUG = env("DEBUG", default=False)
SECRET_KEY = env("SECRET_KEY")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])
HEALTH_CHECK_PATH = env.str("HEALTH_CHECK_PATH", default="health/")
SITE_ID = env("SITE_ID", default=1)
SITE_URL = env("SITE_URL", default="https://barbarzyncy.pl")
ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    "corsheaders",
    "config",
    "django_extensions",
    "core",
    "social",
    "raider_io",
    "battle_net",
    "contact",
    "page",
    "tinymce",
    "recruitment",
    "discord",
    "blog",
    "group",
    "progress",
    "banner",
)

MIDDLEWARE = (
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)

# --- ADMIN ---
LOGIN_REDIRECT_URL = "/admin/"

# --- STATIC FILES ---
STATIC_URL = env("STATIC_URL", default="/static/")
STATIC_ROOT = env("STATIC_ROOT", default="/project/static")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

MEDIA_URL = env("MEDIA_URL", default="/media/")
MEDIA_ROOT = env("MEDIA_ROOT", default="/project/media")

AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME", default=None)
if AWS_STORAGE_BUCKET_NAME is not None:
    INSTALLED_APPS += ("storages",)
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID", default=None)
    AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY", default=None)
    AWS_S3_REGION_NAME = env("AWS_S3_REGION_NAME", default="eu-west-1")
    S3_USE_SIGV4 = True
    AWS_QUERYSTRING_AUTH = False
    AWS_S3_ENDPOINT_URL = f"https://s3.{AWS_S3_REGION_NAME}.amazonaws.com"
    AWS_S3_ADDRESSING_STYLE = env("AWS_S3_ADDRESSING_STYLE", default="virtual")
    AWS_DEFAULT_ACL = env("AWS_DEFAULT_ACL", default=None)

# --- TEMPLATES ---
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [root("templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": (
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.request",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
            )
        },
    }
]


# --- AUTH ---
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# --- DEBUG TOOLBAR ---
ENABLE_DEBUG_TOOLBAR = env.bool("ENABLE_DEBUG_TOOLBAR", default=DEBUG)
if ENABLE_DEBUG_TOOLBAR:
    INSTALLED_APPS += ("debug_toolbar",)
    MIDDLEWARE += ("debug_toolbar.middleware.DebugToolbarMiddleware",)

    INTERNAL_IPS = ("172.18.0.1", "127.0.0.1", "localhost")
    DEBUG_TOOLBAR_CONFIG = {
        "INTERCEPT_REDIRECTS": False,
        "SHOW_TOOLBAR_CALLBACK": lambda *x: True,
    }

# --- CORS ---
CORS_ALLOW_ALL_ORIGINS = env.bool("CORS_ALLOW_ALL", default=False)
CORS_ALLOWED_ORIGINS = env.list("CORS_ORIGIN_WHITELIST", default=[])

# --- TIMEZONE ---
USE_TZ = True
TIME_ZONE = "UTC"

# --- LANGUAGES ---
USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = "pl"

LANGUAGES = (("pl", _("Polish")),)
LOCALE_PATHS = (root("locale"),)

# --- FILE UPLOAD ---
FILE_UPLOAD_MAX_MEMORY_SIZE = 2_621_440  # i.e. 2.5 MB
FILE_UPLOAD_PERMISSIONS = None
FILE_UPLOAD_DIRECTORY_PERMISSIONS = None

# --- DATABASE ---
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": env("DB_NAME", default="barbarzyncy"),
        "USER": env("DB_USER", default="root"),
        "PASSWORD": env("DB_PASSWORD", default="root"),
        "HOST": env("DB_HOST", default="mysql"),
        "PORT": env("DB_PORT", default=3306),
    }
}

# --- RAIDER IO ---
GUILD_NAME = env("GUILD_NAME")
GUILD_REALM = env("GUILD_REALM")
GUILD_REGION = env("GUILD_REGION")
RAIDER_IO_URL = env("RAIDER_IO_URL")

# --- BLIZZARD ---
WOW_CLIENT_ID = env("WOW_CLIENT_ID")
WOW_CLIENT_SECRET = env("WOW_CLIENT_SECRET")

# --- DISCORD ---
DISCORD_CLIENT_ID = env("DISCORD_CLIENT_ID")
DISCORD_CLIENT_SECRET = env("DISCORD_CLIENT_SECRET")
DISCORD_URL = env("DISCORD_URL")
DISCORD_TOKEN = env("DISCORD_TOKEN")
DISCORD_GUILD_ID = env("DISCORD_GUILD_ID")
DISCORD_CATEGORY_ID = env("DISCORD_CATEGORY_ID")
