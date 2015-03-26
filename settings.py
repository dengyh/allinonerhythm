# -*- coding: utf-8 -*-
# Django settings for allinonerhythm project.
import os.path
import socket

DEBUG = True
TEMPLATE_DEBUG = DEBUG
HOST_NAME = "http://allinonerhythm.sinaapp.com/"
PROJECT_PATH = os.path.dirname(globals()["__file__"])

ADMINS = (
    ('dengyh', 'dengyh071@gmail.com'),
)

MANAGERS = ADMINS

IS_SAE = False

if socket.gethostname() != 'dengyh-LIFEBOOK-LH532':
    IS_SAE = True

if IS_SAE:
    # sae的本地文件系统是只读的，修改django的file storage backend为Storage
    DEFAULT_FILE_STORAGE = 'sae.ext.django.storage.backend.Storage'

    MEDIA_ROOT = 'http://allinonerhythm-allinonerhythm.sinaapp.com/media/'
    MEDIA_URL = 'http://allinonerhythm-allinonerhythm.sinaapp.com/media/'

    # 邮件服务
    import sae.const
    EMAIL_ADMIN = "1076142938@qq.com"
    EMAIL_HOST = 'smtp.qq.com'
    EMAIL_PORT = 25
    EMAIL_HOST_USER = '1076142938@qq.com'
    EMAIL_HOST_PASSWORD = '33519000091533'
    DEFAULT_FROM_EMAIL = "1076142938@qq.com"
    EMAIL_USE_TLS = False
    SERVER_EMAIL = DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

    # 数据库
    DATABASES = {
        'default': {
            'ENGINE':   'django.db.backends.mysql',
            'NAME':     sae.const.MYSQL_DB,
            'USER':     sae.const.MYSQL_USER,
            'PASSWORD': sae.const.MYSQL_PASS,
            'HOST':     sae.const.MYSQL_HOST,
            'PORT':     sae.const.MYSQL_PORT,
        }
    }
else :
    # 本地数据库
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'allinonerhythm_test',                      # Or path to database file if using sqlite3.
            'USER': 'root',
            'PASSWORD': '3351900',
            'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
            'PORT': '',                      # Set to empty string for default.
        }
    }

    # Absolute filesystem path to the directory that will hold user-uploaded files.
    # Example: "/var/www/example.com/media/"
    MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media/').replace('\\','/') 

    # URL that handles the media served from MEDIA_ROOT. Make sure to use a
    # trailing slash.
    # Examples: "http://example.com/media/", "http://media.example.com/"
    MEDIA_URL = '/media/'

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'zh-cn'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(PROJECT_PATH, 'static/').replace('\\','/')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'q%2vezkzb&z1m1rju24l@6b%yr!hqeymbxsvhar36!jq9c-4b!'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'allinonerhythm.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'index/templates').replace('\\','/'),
    os.path.join(os.path.dirname(__file__), 'team/templates').replace('\\','/'),
    os.path.join(os.path.dirname(__file__), 'match/templates').replace('\\','/'),
    os.path.join(os.path.dirname(__file__), 'people/templates').replace('\\','/'),
    os.path.join(os.path.dirname(__file__), 'myuser/templates').replace('\\','/'),
    os.path.join(os.path.dirname(__file__), 'static/templates').replace('\\','/'),
    os.path.join(os.path.dirname(__file__), 'static').replace('\\','/'),
    os.path.join(os.path.dirname(__file__), 'backend/templates').replace('\\','/'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

LOGIN_URL = "/user/login/"
LOGOUT_URL = "/user/logout/"

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'match',
    'team',
    'people',
    'myuser',
    'xadmin',
    'index',
    'crispy_forms',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
