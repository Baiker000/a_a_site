from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', views.login_page),
    url(r'logout/$', views.logout_page),
    url(r'^$', views.index),
    url(r'add$', views.involve_to_lottery)
]
