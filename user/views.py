from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from . import models
from . import forms


def index(request):
    pass
    return render(request, 'user/index.html')


def login(request):
    if request.method == "GET":
        login_form = forms.UserForm()
        return render(request, 'user/login.html', {"login_form": login_form})
    elif request.method == "POST":  # 通过post请求读取到了用户名和密码
        login_form = forms.UserForm(request.POST)
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        message = "请检查填写的内容！"
        if login_form.is_valid():  # 换成表单可以避免不明意义的判断
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                current_user = models.User.objects.get(name=username)
                if current_user.password == password:
                    return redirect('/index')  # 正确就重定向到主页，并处于登陆状态
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
            return render(request, 'user/login.html', {"message": message,"login_form": login_form})
        return render(request, 'user/login.html', {"message": message, "login_form": login_form})


def register(request):
    pass
    return render(request, 'user/register.html')


def logout(request):
    pass
    return redirect('/index/')
