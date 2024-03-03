from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=100, unique=True, blank=False, null=False)
	password = models.CharField(max_length=100, blank=False, null=False)
	email = models.EmailField(max_length=150, unique=True)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)

	def __str__(self):
		return self.username

	def Meta():
		pass

class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=150, blank=False, null=False)
	body = models.TextField(max_length=2000)
	date_time = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return self.title

	def Meta():
		pass