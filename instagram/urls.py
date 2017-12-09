from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html',redirect_authenticated_user=True), name= 'login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name= 'logout'),
    url(r'^home/$', views.home, name = 'home'),
    url(r'^uploadFile/$', views.uploadFile, name = 'uploadFile'),
    url(r'^search/$', views.search, name = 'search'),
    url(r'^comment/(?P<id_photo>[\w-]+)/$', views.doComment, name = 'comment'),
    url(r'^like/(?P<id_photo>[\w-]+)/$', views.doLike, name = 'like'),
    url(r'^dislike/(?P<id_photo>[\w-]+)/$', views.removeLike, name = 'dislike'),
    url(r'^(?P<_username>[\w-]+)/$', views.profile, name = 'profile'),
    url(r'^follow/(?P<_username>[\w-]+)/$', views.follow, name = 'follow'),
    url(r'^unfollow/(?P<_username>[\w-]+)/$', views.unfollow, name = 'unfollow'),
]
