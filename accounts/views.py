from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.models import User

def home(request):
    return render(request,"home.html")

def register(request):
    if request.method == "POST":
    
            first_name = request.POST.get("name")
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
    
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
                return redirect("register")
    
           
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists.")
                return redirect("register")
    
            
            user = User.objects.create_user(
                first_name = first_name,
                username=username,
                email=email,
                password=password
            )
            messages.success(
                request,
                "Registration successful. You can now login."
            )
    
            return redirect("login")

    return render(request,"register.html")

def login(request):
    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            auth_login(request, user)

            messages.success(
                request,
                f"Welcome, {user.username}!"
            )

            return redirect("task_list")

        else:

            messages.error(
                request,
                "Invalid username or password."
            )

            return redirect("login")
    return render(request,"login.html")

def user_logout(request):

    logout(request)

    messages.success(
        request,
        "You have been logged out successfully."
    )

    return redirect("login")
