from django.urls import path 
from . import views
from authentication.views import user_logout_view, recruiter_logout_view

urlpatterns = [
    path('<username>/user_profile/', views.user_profile, name='user_profile'),
    path('<username>/applied_jobs/', views.applied_jobs, name='applied_jobs'),
    path('<username>/create_job/', views.create_job, name='create_job'),
    path('<username>/job_list/', views.job_list, name='job_list'),
    path('<username>/job_list_rec/', views.job_list_rec, name='job_list_rec'),
    path("user/logout/",user_logout_view,name="user_logout_view"),
    path("recruiter/logout/",recruiter_logout_view,name="recruiter_logout_view")

]