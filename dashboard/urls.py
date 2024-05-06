from django.urls import path 
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('<username>/user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('<username>/user_profile/', views.user_profile, name='user_profile'),
    path('application_list/', views.application_list, name='application_list'),
    path('create_job/', views.create_job, name='create_job'),
    path('job_list/', views.job_list, name='job_list')
]