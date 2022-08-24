from celery import Celery
from django.conf import settings
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cargobase.settings")

celery_app = Celery("task")
celery_app.config_from_object("django.conf:settings", namespace="CELERY")
