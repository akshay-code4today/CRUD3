"""
Django settings for VMS_project project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-u53s48@)prw=z^i7#6(bqkpa@bg6a7h$j*gwyi6it&a4f97(7%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'VMS_app',
    'crispy_forms',
    'registration',
    #'csp'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'ip_middelware.IPMiddleware',
    #'csp.middleware.CSPMiddleware',
]

ROOT_URLCONF = 'VMS_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                #'csp.context_processors.csp_nonce',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'VMS_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

SESSION_COOKIE_HTTPONLY = True

# uri to report policy violations
# uri to report policy violations
#CSP_REPORT_URI = '<add your reporting uri>'

# default source as self
#CSP_DEFAULT_SRC = ("'self'","https://getbootstrap.com/docs/4.0/")

# style from our domain and bootstrapcdn
#CSP_STYLE_SRC = ("'self'",
                 #"https://getbootstrap.com/docs/4.0/")

# scripts from our domain and other domains
#CSP_SCRIPT_SRC = ["'self'", "'unsafe-inline'", "'unsafe-eval'", "https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/*"]


# images from our domain and other domains
#CSP_IMG_SRC = ("'self'",
               #"www.google-analytics.com",
               #"raw.githubusercontent.com",
               #"googleads.g.doubleclick.net",
               #"https://getbootstrap.com/docs/4.0/")

#loading manifest, workers, frames, etc
#CSP_FONT_SRC = ("'self'","https://getbootstrap.com/docs/4.0/")
#CSP_CONNECT_SRC = ("'self'","www.google-analytics.com","https://getbootstrap.com/docs/4.0/")
#CSP_OBJECT_SRC = ("'self'",)
#CSP_BASE_URI = ("'self'",)
#CSP_FRAME_ANCESTORS = ("'self'",)
#CSP_FORM_ACTION = ("'self'",)
#CSP_INCLUDE_NONCE_IN = ('script-src',)
#CSP_MANIFEST_SRC = ("'self'",)
#CSP_WORKER_SRC = ("'self'",)
#CSP_MEDIA_SRC = ("'self'",)


