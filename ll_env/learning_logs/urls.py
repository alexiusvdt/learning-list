"""Defines URL patterns for learning_logs"""

# needed to map urls to views
from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home. 3args: route, which func to call in views.py, name for url pattern
    path('', views.index, name='index')
]