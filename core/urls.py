from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'test/$', views.test, name='test'),
    url(r'error-404/$', views.error_404, name='error-404'),
    url(r'blank', views.blank, name='blank'),
    url(r'buttons/$', views.buttons, name='buttons'),
    url(r'cards/$', views.cards, name='cards'),
    url(r'charts/$', views.charts, name='charts'),
    url(r'forgot-password/$', views.forgot_password, name='forgot-password'),
    url(r'login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'register/$', views.user_register, name='register'),
    url(r'tables/$', views.tables, name='tables'),
    url(r'u-animation/$', views.u_animation, name='u-animation'),
    url(r'u-border/$', views.u_border, name='u-border'),
    url(r'u-color/$', views.u_color, name='u-color'),
    url(r'u-other/$', views.u_other, name='u-other'),
    # url('logout/', auth.LogoutView.as_view(template_name='user / index.html'), name='logout'),
    url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]
