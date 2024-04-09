# django-blog-noticia/celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Configuração do Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-blog-noticias.settings')

app = Celery('django-blog-noticias')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')