# importing modules and sub-modules here.
from django.contrib import admin
from .models import Post, Profile
from django.contrib.auth.models import User, Group

# registering models
admin.site.register(Post)

# unregistering models
admin.site.unregister(Group)

# mixing profile and user models
class ProfileInline(admin.StackedInline):
	model = Profile

# extends user profile
class UserAdmin(admin.ModelAdmin):
	model = User
	fields = ["username", "password", "first_name", "last_name", "email"]
	inlines = [ProfileInline]

# unregistering models
admin.site.unregister(User)

# registering models
admin.site.register(User, UserAdmin)
# admin.site.register(Profile)