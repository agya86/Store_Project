from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
CSV_URL= 'https://s3.amazonaws.com/test.jampp.com/dmarasca/takehome.csv'


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'storepro.settings')

app = Celery('storeapp')
app.conf.enable_utc = False
app.conf.update(timezone = 'Asia/Kolkata')


app.config_from_object(settings, namespace='CELERY')


# app.conf.beat_schedule = {
#     'update-every-6-hours': {
#         'task': 'storeapp.tasks.read_csv_file',
#         'schedule': 6 * 3600,
#         'args': (CSV_URL)
#     }
    
# }


# Autodiscover tasks in all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request:{self.request!r}')