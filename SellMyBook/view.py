from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from django.http import HttpResponseRedirect
# from django import forms
# #from .forms import UserRegistrationForm
# from django.http import HttpResponse


def home(request):
    # user = authenticate(request, username=username, password=password)
    # if user is not None:
    #     login(request, user)
    print("I am at home page   here we want to print the username of the logged in user.")
    print(request.user.is_authenticated)
    # username = request.POST.get('username')
    # password = request.POST.get('password')
    # print(username + "---" + password)
    # user = authenticate(request, username=username, password=password)
    # if user is not None:
    #     login(request, user)
    return render(request, 'index.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return home(request)
        else:
            message = "Enter valid username and password."
            return render(request, 'login_page.html', {"message": message})
    return render(request, 'login_page.html')


def logout_page(request):
    logout(request)
    return home(request)


def signup_page(request):
    return render(request, 'signup_page.html')


def create_user(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        print(first_name+"---"+last_name+"---"+username+"---"+email+"---"+password+"---"+re_password)
        if password == re_password:
            print("new user added in the field of user table in database.")
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            print(user)
            user.save()
            login(request, user)
    return home(request)


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'books/profile.html')
    else:
        messages.error(request, "You must login first.")
        return render(request, 'login_page.html')
