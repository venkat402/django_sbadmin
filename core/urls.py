from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'test/$', views.test, name='test'),
    url(r'error-404/$', views.error_404, name='error_404'),
    url(r'blank', views.blank, name='blank'),
    url(r'buttons/$', views.buttons, name='buttons'),
    url(r'cards/$', views.cards, name='cards'),
    url(r'charts/$', views.charts, name='charts'),
    url(r'forgot-password/$', views.forgot_password, name='forgot-password'),
    url(r'login/$', views.login, name='login'),
    url(r'register/$', views.register, name='register'),
    url(r'tables/$', views.tables, name='tables'),
    url(r'u-animation/$', views.u_animation, name='u-animation'),
    url(r'u-border/$', views.u_border, name='u-border'),
    url(r'u-color/$', views.u_color, name='u-color'),
    url(r'u-other/$', views.u_other, name='u-other'),
]
