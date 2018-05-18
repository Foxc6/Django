from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^main_app/main/$', views.process),
url(r'^$', views.index),
]