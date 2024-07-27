import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE','myshopss99.settings')

app = Celery('myshopss99')

app.config_from_object('django.conf:settings',namespace='CELERY')


app.autodiscover_tasks()