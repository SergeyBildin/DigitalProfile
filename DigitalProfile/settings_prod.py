DEBUG = False
ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db1',
        'USER': 'digital_profile',
        'PASSWORD': 'zxcvbn10',
        'HOST':'localhost',
        'PORT': '',
    }
}

