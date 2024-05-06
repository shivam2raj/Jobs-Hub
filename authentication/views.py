from django.shortcuts import render

# Create your views here.
# Import necessary modules and models
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password,check_password
from .models import Recruiter
from dashboard.models import UserProfile

def user_login_page(request):

	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		

		if not User.objects.filter(username=username).exists():

			messages.error(request, 'Invalid Username')
			return redirect('/user/login/')
		

		user = authenticate(username=username, password=password)
		
		if user:

			login(request, user)
			return redirect(f"/{username}/user_dashboard")
		else:

			messages.error(request, "Invalid Password")
			return redirect('/user/login/')


	return render(request, 'user_login.html')


def logout_view(request):
	logout(request)
	return redirect("/user/login/")

def user_register_page(request):

	if request.method == 'POST':
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		email = request.POST.get('email')
		username = request.POST.get('username')
		password = request.POST.get('password')
		

		user = User.objects.filter(username=username)
		
		if user.exists():

			messages.info(request, "Username already taken!")
			return redirect('/user/register/')
		

		user = User.objects.create_user(
			first_name=first_name,
			last_name=last_name,
			email=email,
			username=username
		)
		
		user.set_password(password)
		user.save()

		UserProfile.objects.create(user= user)
		
		messages.info(request, "Account created Successfully!")
		return redirect('/user/login/')

	return render(request, 'user_reg.html')

def home(request):
	return render(request, 'home.html')


def recruiter_register_page(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        company_name = request.POST.get("company_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if Recruiter.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return redirect("recruiter_register")

        if Recruiter.objects.filter(email=email).exists():
            messages.error(request, "Email is already taken.")
            return redirect("recruiter_register")

        if (
            first_name
            and last_name
			and company_name
            and username
            and email
            and password
        ):
            recruiter = Recruiter(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
				company_name=company_name,
                password=password,
            )
            recruiter.save()
        else:
            messages.error(request, "fill all the details !!!")
            return redirect("recruiter_register")

        messages.success(request, "Registration Successful")
        return redirect("recruiter_login")

    else:
        return render(request, "recruiter_register.html")


def recruiter_login_page(request):

	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')

		
		user_exist= Recruiter.objects.get(username=username)
		if(user_exist and user_exist.password ==password ):
			return redirect('dashboard')
		else:
			return redirect('login')
			


	return render(request, 'recruiter_login.html')




