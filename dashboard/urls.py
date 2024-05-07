from django.urls import path 
from . import views
from authentication.views import user_logout_view, recruiter_logout_view

urlpatterns = [
    path('<username>/recruiter_dashboard/', views.recruiter_dashboard, name='recruiter_dashboard'),
    path('<username>/user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('<username>/user_profile/', views.user_profile, name='user_profile'),
    path('application_list/', views.application_list, name='application_list'),
    path('create_job/', views.create_job, name='create_job'),
    path('<username>/job_list/', views.job_list, name='job_list'),
    path("user/logout/",user_logout_view,name="user_logout_view"),
    path("recruiter/logout/",recruiter_logout_view,name="recruiter_logout_view")

]