"""
Django settings for ucbc project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'WILL_HAVE_TO_CHANGE_THIS_BAD_BOY'#FIXME

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True #FIXME change this
TEMPLATE_DEBUG = DEBUG #FIXME change this

ALLOWED_HOSTS = ['*']#FIXME you have to remove this

#ADMINS = ( ('NAME', 'EMAIL'), ( 'NAME', 'EMAIL') )
# Application definition

INSTALLED_APPS = (
    #'grappelli.dashboard',
    #'grappelli',
    'filebrowser',
    #'django_admin_bootstrapped.bootstrap3',
    #'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #JEFF'django.contrib.sites',
    #JEFF'django.contrib.flatpages',
    'simple',
    'django_evolution',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ucbc.urls'

WSGI_APPLICATION = 'ucbc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#JEFF
SITE_ID = 1

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

#http://stackoverflow.com/questions/5871730/need-a-minimal-django-file-upload-example


# FIXME fix this guy
STATIC_ROOT = 'staticfiles/'
STATIC_URL = '/static/'
MEDIA_ROOT = 'mediaroot/'
MEDIA_URL = '/media/'
FILEBROWSER_MEDIA_ROOT = 'mediaroot/'
#FLIEBROWSWE_ROOT = '/mediaroot'
FILEBROWSER_VERSIONS_BASEDIR = '_versions'


TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates') ]

STATICFILES_DIRS = (
#  os.path.join(BASE_DIR, 'staticfiles'),
#  '~Projects/UCBC/ucbc/staticfiles/',
#    os.path.join(BASE_DIR, "static"),
os.path.join(BASE_DIR, 'bootstrap-3.2.0-dist'),
)

#STATICFILES_FINDERS = (
#    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.FileSystemFinder',
#)

#TEMPLATE_CONTEXT_PROCESSORS = (
#    'django.contrib.auth.context_processors.auth',
#    'django.core.context_processors.request',
#)

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_PORT = 587
#EMAIL_HOST = "smtp.gmail.com"

#EMAIL_USE_TLS = True
#DEFAULT_FROM_EMAIL = ''
#SERVER_EMAIL = ''
#EMAIL_HOST_USER = ''
#EMAIL_HOST_PASSWORD = ''
