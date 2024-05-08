from django.urls import reverse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile,Jobpost,JobApplication
from authentication.models import Recruiters


# Create your views here.
@login_required(login_url="/recruiter/login/")
def recruiter_dashboard(request, username):
    user = request.user

    return render(request, 'dashboard.html', {'user': user})

def create_job(request):

    username = request.user.username

    if request.method == 'POST':
        title = request.POST.get('title')
        jobDescription = request.POST.get('jobDescription')
        jobRequirement = request.POST.get('jobRequirement')
        salary = request.POST.get('salary')
        jobtype = request.POST.get('jobtype')
        location = request.POST.get('location')

        Jobpost.objects.create(title=title, jobDescription=jobDescription, jobRequirement=jobRequirement, salary=salary, jobtype=jobtype, location=location)

        return redirect('/' + username + '/recruiter_dashboard')
    return render(request, 'create-job.html')

def job_list(request, username):

    jobposts = Jobpost.objects.all()
    username = request.user.username

    users = User.objects.filter(username=username)
    if request.method == 'POST':
        jobpostid = request.POST.get('JobpostId')

        if JobApplication.objects.filter(JobpostId=jobpostid, UserApplied=username).exists():

            messages.error(request, 'User has already applied')
        else:
            JobApplication.objects.create(JobpostId=jobpostid, UserApplied=username)
            return redirect('/' + username + '/applied_jobs')

    context = {'jobposts': jobposts, 'users': users}

    return render(request,'job-list.html', context)



def applied_jobs(request, username):

    job_applications = JobApplication.objects.filter(UserApplied=username)

    job_posts = Jobpost.objects.filter(id__in=[job_application.JobpostId for job_application in job_applications])

    context = {'jobApplications': job_applications, 'jobPosts': job_posts}
    return render(request, 'applied_jobs.html', context)


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
        age = request.POST.get('age')
        education = request.POST.get('education')
        work_experience = request.POST.get('work_experience')
        skills = request.POST.get('skills')
        certifications = request.POST.get('certifications')
        phone_number = request.POST.get('phone-number')
        bio = request.POST.get('bio')
        cv = request.POST.get('cv')

        user = User.objects.get(username=username)

        profile = UserProfile.objects.get(user=user)
        profile.address= address
        profile.age = age
        profile.education = education
        profile.work_experience = work_experience
        profile.skills = skills
        profile.certifications = certifications
        profile.cv = cv
        profile.phone_number = phone_number
        profile.bio = bio

        profile.save()

    context = {'profile': profile, 'user': user}

    return render(request,'user-profile.html', context)
