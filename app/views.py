from django.shortcuts import render
from .models import User, Post

# Create your views here.
def index(request):
		return render(request, "index.html", {})

def register_login(request):
	all_users = User.objects.all()
	all_posts = Post.objects.all()
	return render(request, "register_login.html", {"users": all_users, "posts": all_posts})

def login(request):
	return render(request, "login.html", {})

def signup(request):
	return render(request, "signup.html", {})

def comming_soon(request):
	return render(request, "comming_soon.html", {})