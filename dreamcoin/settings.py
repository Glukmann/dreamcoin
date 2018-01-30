# -*- coding: utf-8 -*-
"""
Django settings for dreamcoin project.

"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2*_)ma(s6ggon16#lttsuo2)10w@8z-yuv@%+62#^8$@ggijk('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

NEED_REGENERATE_MODELS = ['Page', ]


ADMINS = (
    ('admin', 'admin@gmail.com'),
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dreamcoin.apps.DreamcoinConfig',

    ###===user-generated-apps===###
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'dreamcoin/templates')],
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


ROOT_URLCONF = 'dreamcoin.urls'

WSGI_APPLICATION = 'dreamcoin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#         'NAME': '{{ dreamcoin }}',          # Or path to database file if using sqlite3.
#         'USER': 'root',                        # Not used with sqlite3.
#         'PASSWORD': 'changeme',                  # Not used with sqlite3.
#         'HOST': '82.151.212.181',                # Set to empty string for localhost. Not used with sqlite3.
#         'PORT': '3306',                        # Set to empty string for default. Not used with sqlite3.
#         'TEST_CHARSET': 'utf8',
#         'TEST_COLLATION': 'utf8_general_ci',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'dreamcoin',
#         'USER' : 'dreamcoin',
#         'PASSWORD' : 'LhbvRjby',
#         'HOST' : '127.0.0.1',
#         'PORT' : '5432',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/{{ docs_version }}/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Asia/Yekaterinburg'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images) and media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'dreamcoin/public/media')
MEDIA_URL = '/media/'


STATIC_ROOT = os.path.join(BASE_DIR, 'dreamcoin/public/static')
STATIC_URL = '/static/'


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "dreamcoin/static"),
)


if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


NO_IMG_PATH = 'no_img.png'


TINYMCE_DEFAULT_CONFIG = {
    'plugins': "safari,pagebreak,style,layer,table,save,advhr,advimage,advlink,emotions,iespell,inlinepopups,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template",
    'theme': "advanced",
    'theme_advanced_buttons1': "bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,|,styleselect,formatselect",
    'theme_advanced_buttons2': "cut,copy,paste,pasteword,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,anchor,image,cleanup,code,|,forecolor,backcolor",
    'theme_advanced_buttons3': "tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,charmap,iespell,media,advhr,|,fullscreen",
    'theme_advanced_toolbar_location': "top",
    'theme_advanced_toolbar_align': "left",
    'theme_advanced_statusbar_location': "bottom",
    'theme_advanced_resizing': "true",
    'relative_urls': False,
}
