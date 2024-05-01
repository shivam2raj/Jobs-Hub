from django.contrib import admin 
from django.urls import path	
from authentication.views import *
from django.conf import settings 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 


urlpatterns = [
	path('user/login/', user_login_page, name='user_login_page'), 
	path('user/register/', user_register_page, name='user_register'), 
]


urlpatterns += staticfiles_urlpatterns()
