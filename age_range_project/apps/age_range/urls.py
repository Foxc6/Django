from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^home$', views.home),
    url(r'^logout$', views.logout),
    url(r'^under_10$', views.under_10),
    url(r'^eleven_18$', views.eleven_18),
    url(r'^nineteen_24$', views.nineteen_24),
    url(r'^twentyfive_35$', views.twentyfive_35),
    url(r'^thirtysix_50$', views.thirtysix_50),
    url(r'^over_51$', views.over_51),
    url(r'^users/(?P<id>\d+)/delete/$', views.delete, name='delete'),
]