from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'test/$', views.test, name='test'),
    url(r'error-404/$', views.error_404, name='error-404'),
    url(r'blank', views.blank, name='blank'),
    url(r'buttons/$', views.buttons, name='buttons'),
    url(r'cards/$', views.cards, name='cards'),
    url(r'charts/$', views.charts, name='charts'),
    url(r'forgot-password/$', views.password_reset_request, name='forgot-password'),
    url(r'login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'register/$', views.user_register, name='register'),
    url(r'tables/$', views.tables, name='tables'),
    url(r'employee_form/$', views.employee_form, name='employee_form'),
    url(r'cards_form/$', views.cards_form, name='cards_form'),
    url(r'graph_form/$', views.graphs_form, name='graph_form'),
    url(r'settings_form/$', views.settings_form, name='settings_form'),
    url(r'u-animation/$', views.u_animation, name='u-animation'),
    url(r'u-border/$', views.u_border, name='u-border'),
    url(r'u-color/$', views.u_color, name='u-color'),
    url(r'u-other/$', views.u_other, name='u-other'),
    # url('logout/', auth.LogoutView.as_view(template_name='user / index.html'), name='logout'),
    url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),

]
