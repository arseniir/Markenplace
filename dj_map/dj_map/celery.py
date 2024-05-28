import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj_map.settings')

app = Celery('dj_map')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'sales_day': {
        'task': 'ProjectB.tasks.sale_beet_task',
        # 'schedule': crontab(minute='*/2'),
        'schedule': crontab(day_of_week='saturday')
    },
}


