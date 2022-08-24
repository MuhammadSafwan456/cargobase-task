from django.contrib import admin
from django.urls import path, include

from .views import ScrapView, InfoView, StatusView

urlpatterns = [
    path("scrap/", ScrapView.as_view(), name="scrap"),
    path("info/", InfoView.as_view(), name="info"),
    path("<uuid:task_id>/status/", StatusView.as_view(), name="status"),
]
