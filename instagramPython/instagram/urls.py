from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login', views.login, name = 'login'),
    url(r'^createUser', views.createUser),
    url(r'^mainPage/(?P<id_user>\d+)/$', views.mainPage, name = 'mainPage'),
    url(r'^profile/(?P<id_user>\d+)/$', views.profile, name = 'profile'),
    url(r'^uploadPhoto/(?P<id_user>\d+)/$', views.uploadPhoto, name = 'uploadPhoto'),
    url(r'^uploadFile/(?P<id_user>\d+)/$', views.uploadFile, name = 'uploadFile'),
    url(r'^search/(?P<id_user>\d+)/$', views.search, name = 'search'),
    url(r'^follow/$', views.follow, name = 'follow'),
]
