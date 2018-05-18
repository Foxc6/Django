from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.welcome),
    url(r'^index$', views.index),
    url(r'^create_pet$', views.create_pet),
]