from django.urls import path 
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create_job/', views.create_job, name='create_job'),
    path('job_list/', views.job_list, name='job_list')
]