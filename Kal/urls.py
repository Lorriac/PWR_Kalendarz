# Kal/urls.py

from django.conf.urls import url
from . import views

app_name = 'Kal'
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
]