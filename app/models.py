from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
	age = models.PositiveIntegerField(blank=True, null=True)
	bio = models.TextField(max_length=500, blank=True)

# class UserProfile(models.Model):
# 	user = models.OneToOneField(User, on_delete=models.CASCADE)
# 	bio = models.TextField(blank=True)
# 	birthday = models.CharField(max_length=20, blank=True, null=True)
# 	profile_picture = models.ImageField(upload_to="profile_pics/", blank=True)

# 	def __str__(self):
# 		return self.user.username

# class Post(models.Model):
# 	user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
# 	title = models.CharField(max_length=150, blank=False, null=False)
# 	body = models.TextField(max_length=2000)
# 	date_time = models.DateTimeField(blank=True, null=True)
# 	likes = models.ManyToManyField(User, related_name="post_likes", blank=True)

# 	def __str__(self):
# 		return self.title