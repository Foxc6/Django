from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^new/$', views.new),
    url(r'^users/edit/(?P<id>\d+)/$', views.edit, name='edit'),
    url(r'^users/show/(?P<id>\d+)/$', views.show, name='show'),
    url(r'^users/(?P<id>\d+)/delete/$', views.delete, name='delete'),
    url(r'^update/(?P<id>\d+)/$', views.update, name='update'),
]