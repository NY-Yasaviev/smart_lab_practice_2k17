from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout')
]
