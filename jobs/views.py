from django.shortcuts import render
from .models import Jobs
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.models import User

# Create your views here.
# this is the function for the form 
class NewJobsForm(forms.Form):
    Title = forms.CharField(label="Title")
    Description = forms.CharField(max_length=600)
    Location = forms.CharField(max_length=20)
    Price = forms.IntegerField()
# the function to load the  main page 
def index(request):
    return render(request, "jobs/index.html", {
        "Jobs": Jobs.objects.all()
    })
# function to load the  job detail page 
def detail(request, job_id):
    job = Jobs.objects.get(id=job_id)
    return render(request, "jobs/detail.html", {
        "job": job
    })
#function to add new jobs to this website 
def new(request):
    if request.method == "POST":
        form = NewJobsForm(request.POST)
        if form.is_valid():
            job = Jobs(
                Title=form.cleaned_data["Title"],
                Description=form.cleaned_data["Description"],
                Location=form.cleaned_data["Location"],
                Price=form.cleaned_data["Price"]
            )
            job.save()
            return HttpResponseRedirect(reverse("jobs:index"))  # takes the user back to the the home page 
    else:
        form = NewJobsForm()
    return render(request, "jobs/new.html", {
        "form": form
    })
# function to load the  login page  and also does the authentication
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("jobs:index"))  
        else:
            return render(request, "jobs/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "jobs/login.html")
# the function  to logout the user 
def logout_view(request):
    logout(request)
    return render(request,"jobs/out.html")
# function to register new users to this website 
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "jobs/register.html", {
                "message": "Passwords must match."
            })
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "jobs/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("jobs:index"))  
    else:
        return render(request, "jobs/register.html")
    

    # function to load the profile 
def profile(request):
    return render(request,"jobs/profile.html")