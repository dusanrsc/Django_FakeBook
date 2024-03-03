# importing modules and sub-modules here.
from django.contrib import admin

# importing sub-modules for unregistration.
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

# Unregister your models here.
admin.site.unregister(Group)
admin.site.unregister(User)

# importing local models
from .models import User, Post

# Register your local models here.
admin.site.register(User)
admin.site.register(Post)