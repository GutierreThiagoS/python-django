from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

from . import views 

# HTTP Request e Response
# MVT (MVC)

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='home'),
    path('<int:id>/', views.post, name='post'),
    path('exemplo/', views.exemplo, name='exemplo'),
]
