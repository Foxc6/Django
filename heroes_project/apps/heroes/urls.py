from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.welcome),
    url(r'^hero_index$', views.hero_index),
    url(r'^show_hero/hero/(?P<id>\d+)/$', views.show_hero),
    url(r'^new_hero$', views.new_hero),
    url(r'^create_hero$', views.create_hero),
    url(r'^new_power$', views.new_power),
    url(r'^create_power$', views.create_power),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
]