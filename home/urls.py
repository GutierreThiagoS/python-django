from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

from . import views

# HTTP Request e Response
# MVT (MVC)
app_name = 'home'


urlpatterns = [
    path('', views.index, name='home'),
]
