import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','DigitalProfile.settings')

app = Celery('DigitalProfile')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()