from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.welcome),
    url(r'^index$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^add_friend/new_friend/(?P<id>\d+)/$', views.add_friend),
    url(r'^remove_friend/remove_friend/(?P<id>\d+)/$', views.remove_friend),
    url(r'^show_user/user/(?P<id>\d+)/$', views.show_user),
]