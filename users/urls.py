"""Users URL Configuration"""

from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    # include default authorization
    path('', include('django.contrib.auth.urls')),
    # registration
    path('register/', views.register, name='register')
]