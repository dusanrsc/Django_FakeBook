from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

# Create your views here.
@login_required(login_url="login_user")
def index(request):
	return render(request, 'index.html')

def register_user(request):
	form = CreateUserForm()
	if request.method == "POST":
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("login_user")

	return render(request, "register_user.html", {"registerform": form})

def login_user(request):
	form = LoginForm()
	if request.method == "POST":
		form = LoginForm(request, data=request.POST)
		if form.is_valid():
			username = request.POST.get("username")
			password = request.POST.get("password")
			user = authenticate(request, username=username, password=password)
			if user is not None:
				auth.login(request, user)
				return redirect("index")

	return render(request, "login_user.html", {"loginform": form})

def logout_user(request):
	auth.logout(request)
	return redirect("login_user")

def comming_soon(request):
	return render(request, "comming_soon.html", {})