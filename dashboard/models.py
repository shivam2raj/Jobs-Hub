from django.db import models
from authentication.models import Recruiters
from django.contrib.auth.models import User

# Create your models here.

class Jobpost(models.Model):
    recruiter = models.OneToOneField(Recruiters, on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=200,null=True,blank=True)
    jobDescription=models.CharField(max_length=200,null=True,blank=True)
    jobRequirement=models.CharField(max_length=200,null=True,blank=True)
    jobtype=models.CharField(max_length=200,null=True,blank=True)
    salary=models.IntegerField(null=True,blank=True)
    location=models.CharField(max_length=200,null=True,blank=True)
    pub_date= models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.title

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255,null=True,blank=True)
    date_of_birth = models.DateField(null=True,blank=True)
    education = models.TextField(null=True,blank=True)
    work_experience = models.TextField(null=True,blank=True)
    skills = models.TextField(null=True,blank=True)
    certifications = models.TextField(null=True,blank=True)
    cv = models.FileField(upload_to='cv/%Y/%m/%d',null=True,blank=True)

    def __str__(self):
        return self.user.username

class JobApplication(models.Model):
    
    jobpost = models.OneToOneField(Jobpost, on_delete=models.CASCADE,null=True)
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE,null=True)
    JobpostId = models.IntegerField(null=True,blank=True)
    UserApplied = models.TextField(null=True,blank=True)
    ApplyDate = models.DateField(auto_now_add=True,null=True,blank=True)

    def _str_(self):
        return self.UserApplied