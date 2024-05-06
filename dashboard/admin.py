from django.contrib import admin
from .models import Jobpost, UserProfile, JobApplication

# Register your models here.
admin.site.register(Jobpost)
admin.site.register(UserProfile)
admin.site.register(JobApplication)