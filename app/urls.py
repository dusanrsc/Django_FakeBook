"""
URL configuration for FakeBook project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),

    path("register_user", views.register_user, name="register_user"),
    path("login_user", views.login_user, name="login_user"),

    path("search_user", views.search_user, name="search_user"),
    path("friends", views.friends, name="friends"),
    path("video", views.video, name="video"),
    path("market", views.market, name="market"),
    path("groups", views.groups, name="groups"),

    path("profile", views.profile, name="profile"),
    path("messages", views.messages, name="messages"),
    path("settings", views.settings, name="settings"),
    path("logout_user", views.logout_user, name="logout_user"),

    path("comming_soon", views.comming_soon, name="comming_soon"),
]
