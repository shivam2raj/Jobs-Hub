from django.shortcuts import render, redirect
from .models import Jobpost


# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')

def create_job(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        jobDescription = request.POST.get('jobDescription')
        jobtype = request.POST.get('jobtype')
        location = request.POST.get('location')

        Jobpost.objects.create(title=title, jobDescription=jobDescription, jobtype=jobtype, location=location)

        return redirect('dashboard')
    return render(request, 'create-job.html')

def job_list(request):

    jobposts = Jobpost.objects.all()
    return render(request,'job-list.html',{'jobposts': jobposts})
