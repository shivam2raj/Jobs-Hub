from django.db import models
from authentication.models import Recruiter
from django.contrib.auth.models import User

# Create your models here.

class Jobpost(models.Model):
    title=models.CharField(max_length=200)
    jobDescription=models.CharField(max_length=200)
    jobtype=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    pub_date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Title: {self.title}, Description: {self.jobDescription}, Type: {self.jobtype}, Location: {self.location}, Date: {self.pub_date}"




