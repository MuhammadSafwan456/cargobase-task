from celery import Celery
from django.conf import settings
import os

settings.configure()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cargobase.settings")

celery_app = Celery("task")
celery_app.config_from_object("django.conf:settings", namespace="CELERY")
print(celery_app)
print(dir(celery_app))
print("***********************8",celery_app.conf)
print("++++++++++++++++++++++++++++++++",celery_app.conf.broker_read_url)
celery_app.autodiscover_tasks()
