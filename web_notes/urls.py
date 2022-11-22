"""web_notes URL Configuration"""

from django.urls import path
from . import views

from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView


app_name = 'web_notes'
urlpatterns = [
    # Homepage
    path('', views.index, name='index'),

    # page with topics
    path('topics/', views.topics, name='topics'),

    # page with single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # page for adding new topic
    path('new_topic/', views.new_topic, name='new_topic'),

    # page for new note
    path('new_note/<int:topic_id>/', views.new_note, name='new_note'),

    # page for editing notes
    path('edit_note/<int:note_id>/', views.edit_note, name='edit_note'),

]

