from django.urls import path
from .views import *
urlpatterns = [
    path("home/",home),
    path("register/",register, name="register"),
    path("login/",login, name="login"),
    path("logout/",user_logout, name="logout"),
]