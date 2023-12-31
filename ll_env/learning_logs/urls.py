"""Defines URL patterns for learning_logs"""

# needed to map urls to views
from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home. 3args: route, which func to call in views.py, name for url pattern
    path('', views.index, name='index'),
    # page to show all topics
    path('topics/', views.topics, name='topics'),
    # detail page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # new entries must associate with a topic so we need the topic_id arg in the url
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # page for editing an entry
    path('edit_entry<int:entry_id>/', views.edit_entry, name='edit_entry'),
]