from django.contrib import admin 
from django.urls import path	
from authentication.views import *
from django.conf import settings 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 


urlpatterns = [
	path('user/login/', user_login_page, name='user_login'), 
	path('recruiter/login/', recruiter_login_page, name='recruiter_login'), 
	path('user/register/', user_register_page, name='user_register'), 
	path('recruiter/register/', recruiter_register_page, name='recruiter_register'), 
	path('', home, name='home'), 
]


urlpatterns += staticfiles_urlpatterns()
