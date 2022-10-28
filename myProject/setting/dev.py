from myProject.settings import *

SECRET_KEY = 'django-insecure-tyh7n1f=)h9gsjkct=-9=3*yi9@j01&_yggba$wnqe&+r*&6+a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

INTERNAL_IPS = [
    "127.0.0.1",
]

STATIC_ROOT = BASE_DIR/'statics'
MEDIA_ROOT = BASE_DIR/'medias'

STATICFILES_DIRS = [
    BASE_DIR / "myApp/static"
]
SITE_ID = 2



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

X_FRAME_OPTIONS='SAMEORIGIN'

