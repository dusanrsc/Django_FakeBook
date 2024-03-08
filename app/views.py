from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

from django.db.models import Q

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

def search_user(request):
	if request.method == "POST":
		search = request.POST["search"]
		searched = User.objects.filter(Q(username__contains=search) | Q(first_name__contains=search) | Q(last_name__contains=search))

		return render(request, "search_user.html", {"search": search, "searched": searched})
	else:
		return render(request, "search_user.html", {})

def comming_soon(request):
	return render(request, "comming_soon.html", {})