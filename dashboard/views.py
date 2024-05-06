from django.urls import reverse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile,Jobpost,JobApplication


# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')

def create_job(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        jobDescription = request.POST.get('jobDescription')
        jobRequirement = request.POST.get('jobRequirement')
        salary = request.POST.get('salary')
        jobtype = request.POST.get('jobtype')
        location = request.POST.get('location')

        Jobpost.objects.create(title=title, jobDescription=jobDescription, jobtype=jobtype, location=location)

        return redirect('dashboard')
    return render(request, 'create-job.html')

def job_list(request):

    jobposts = Jobpost.objects.all()
    username = request.user.username
    
    if request.method == 'POST':
        jobpostid = request.POST.get('JobpostId')
        print("control reaches here")

        if JobApplication.objects.filter(JobpostId=jobpostid, UserApplied=username).exists():

            messages.error(request, 'User has already applied')
        else:
            JobApplication.objects.create(JobpostId=jobpostid, UserApplied=username)   

    context = {'jobposts': jobposts}

    return render(request,'job-list.html', context)

def application_list(request):

    username = request.user.username

    jobApplications = JobApplication.objects.get(UserApplied=username)

    print(jobApplications)

    return render(request,'applicant-list.html', {'jobApplications': jobApplications})



@login_required(login_url="/user/login/")
def user_dashboard(request, username):

    user = request.user
    data = UserProfile.objects.get(user=user)

    context = {'user': user, 'data': data}

    return render(request, 'user_dashboard.html', context)

def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(UserProfile, user=user)
    if request.method == 'POST':
        address = request.POST.get('address')
        # date_of_birth = request.POST.get('date_of_birth')
        education = request.POST.get('education')
        work_experience = request.POST.get('work_experience')
        skills = request.POST.get('skills')
        certifications = request.POST.get('certifications')
        cv = request.POST.get('cv')

        user = User.objects.get(username=username)

        profile = UserProfile.objects.get(user=user)
        profile.address= address
        # profile.date_of_birth=date_of_birth
        profile.education = education
        profile.work_experience = work_experience
        profile.skills = skills
        profile.certifications = certifications
        profile.cv = cv

        profile.save()

    context = {'profile': profile, 'user': user}

    return render(request,'user-profile.html', context)



