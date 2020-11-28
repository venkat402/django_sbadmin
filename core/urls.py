from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'test/$',views.test),
    url(r'error-404/$', views.error_404),
    url(r'blank/$', views.blank),
    url(r'buttons/$', views.buttons),
    url(r'cards/$', views.cards),
    url(r'charts/$', views.charts),
    url(r'forgot-password/$', views.forgot_password),
    url(r'login/$', views.login),
    url(r'register/$', views.register),
    url(r'tables/$', views.tables),
    url(r'u-animation/$', views.u_animation),
    url(r'u-border/$', views.u_border),
    url(r'u-color/$', views.u_color),
    url(r'u-other/$', views.u_other),
]

