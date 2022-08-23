from django.contrib import admin
from django.urls import path,include

from  .views import ScrapView, InfoView
urlpatterns = [
    path('scrap/', ScrapView.as_view(), name='scrap'),
    path('info/', InfoView.as_view(), name='info'),
]
