# importing modules and sub-modules here
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# post model
class Post(models.Model):
	user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
	title = models.CharField(max_length=150, blank=False, null=False)
	body = models.TextField(max_length=2000)
	date_time = models.DateTimeField(blank=True, null=True)
	likes = models.ManyToManyField(User, related_name="post_likes", blank=True)

	def __str__(self):
		return self.title

# profile model
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	follows = models.ManyToManyField("self", related_name="followed_by", symmetrical=False, blank=True)
	image = models.ImageField(upload_to="profile_pics/", blank=True, null=True)

	def __str__(self):
		return self.user.username