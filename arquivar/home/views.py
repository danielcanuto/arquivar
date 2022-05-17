from django.shortcuts import render, redirect
from django.contrib.auth import logout, login


def home(request):
    return render(request, 'home.html')


def my_logout(request):
    logout(request)
    return redirect('home')

# def my_login(request):
#     login(request)
#     return("admin")
