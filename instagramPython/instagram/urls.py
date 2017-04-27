from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='instagram/login.html'), name= 'login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='instagram/index.html'), name= 'logout'),
    url(r'^createUser', views.createUser),
    url(r'^mainPage/$', views.mainPage, name = 'mainPage'),
    url(r'^profile/$', views.profile, name = 'profile'),
    url(r'^uploadPhoto/$', views.uploadPhoto, name = 'uploadPhoto'),
    url(r'^uploadFile/$', views.uploadFile, name = 'uploadFile'),
    url(r'^search/$', views.search, name = 'search'),
    url(r'^follow/$', views.follow, name = 'follow'),
]
