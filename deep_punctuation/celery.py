import os

from celery import Celery
from django.conf import settings

# Need to set DJANGO_SETTINGS_MODULE env variable to use settings.* in this file
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'deep_punctuation.settings')

app = Celery('deep_punc')

# broker url format: redis://:password@hostname:port/db_number
app.conf.broker_url = 'redis://' + settings.REDIS_HOST + ':6379/0'
app.autodiscover_tasks()