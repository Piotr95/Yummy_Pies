from django.conf.urls import url
from django.contrib import admin
from UserManagement import views
from django.contrib.auth import views as auth_views
app_name = 'UserManagement'
urlpatterns = [
    url(r'^register$', views.register, name="register"),
    url(r'^login$', views.login, name='login'),
    url(r'^logout_user/$', views.log_out, name='logout'),
]