from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^users/register/$', views.create),
url(r'^users/login/$', views.login),
url(r'^users/new/$', views.create),
url(r'^users/$', views.index),
]