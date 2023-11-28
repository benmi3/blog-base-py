"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-669#@_x#laaws$is=+i+^zd@#-+d^bi9ti9-cv26*6dgu*rx@o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'debug_toolbar',                # For debug
    'polls.apps.PollsConfig',       # Polls
    'posts.apps.PostsConfig',       # Posts
    'django.contrib.admin',         # Default
    'django.contrib.auth',          # Default
    'django.contrib.contenttypes',  # Default
    'django.contrib.sessions',      # Default
    'django.contrib.messages',      # Default
    'django.contrib.staticfiles',   # Default
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',            # Default
    'django.contrib.sessions.middleware.SessionMiddleware',     # Default
    'django.middleware.common.CommonMiddleware',                # Default
    'django.middleware.csrf.CsrfViewMiddleware',                # Default
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Default
    'django.contrib.messages.middleware.MessageMiddleware',     # Default
    'django.middleware.clickjacking.XFrameOptionsMiddleware',   # Default
    # If you add enocing middleware ex GZipMiddleware, add before this
    'debug_toolbar.middleware.DebugToolbarMiddleware',         # For debug
]

ROOT_URLCONF = 'blog_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'blog_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tokyo'  # Default UTC

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# internal ip
INTERNAL_IPS = [
    "127.0.0.1",
]
"""
# If using Docker the following will set your INTERNAL_IPS correctly in Debug mode:
if DEBUG:
    import socket  # only if you haven't already imported this
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]
"""
