from django.urls import re_path
from . import views


app_name = 'django_auth_oidc'
urlpatterns = [
	re_path(r'^$', views.login, name='login'),
	re_path(r'^done/$', views.callback, name='login-done'),
	re_path(r'^logout/$', views.logout, name='logout'),
]
