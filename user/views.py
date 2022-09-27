from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect


def index(request):
    pass
    return render(request, 'user/index.html')


def login(request):
    pass
    return render(request, 'user/login.html')


def register(request):
    pass
    return render(request, 'user/register.html')


def logout(request):
    pass
    return redirect('/index/')
