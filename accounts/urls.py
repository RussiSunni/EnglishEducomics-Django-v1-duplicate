from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views


app_name='accounts'

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    #url(r'^login/$', views.login, name='login'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^register/$', views.register, name='register'),

]