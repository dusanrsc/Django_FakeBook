from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput

class CreateUserForm(UserCreationForm):
	first_name = forms.CharField(label="", widget=TextInput(attrs={"placeholder": "First name", "class": "form-control", "style": "width:340px"}))
	last_name = forms.CharField(label="", widget=TextInput(attrs={"placeholder": "Last name", "class": "form-control", "style": "width:340px"}))
	username = forms.CharField(label="", widget=TextInput(attrs={"placeholder": "Username", "class": "form-control", "style": "width:340px"}))
	email = forms.CharField(label="", widget=TextInput(attrs={"placeholder": "Email Address", "class": "form-control", "style": "width:340px"}))
	password1 = forms.CharField(label="", widget=PasswordInput(attrs={"placeholder": "Password", "class": "form-control", "style": "width:340px"}))
	password2 = forms.CharField(label="", widget=PasswordInput(attrs={"placeholder": "Password Confirmation", "class": "form-control", "style": "width:340px"}))

	class Meta:
		model = User
		fields = ["first_name", "last_name", "username", "email", "password1", "password2"]

class LoginForm(AuthenticationForm):
	username = forms.CharField(label="", widget=TextInput(attrs={"placeholder":"Username", "class":"form-control", "style": "width:395px", "style": "height:50px"}))
	password = forms.CharField(label="", widget=PasswordInput(attrs={"placeholder":"Password", "class":"form-control", "style": "width:395px", "style": "height:50px"}))