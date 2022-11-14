from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab

from config.settings import CELERY_BROKER_URL

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery("config", broker=CELERY_BROKER_URL, include=['core.tasks'])
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-sum': {
        'task': "core.tasks.main",
        'schedule': crontab(day_of_week='*', hour=7),
    },
}