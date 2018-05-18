from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.welcome),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^index$', views.index),
    url(r'^logout$', views.logout),
]