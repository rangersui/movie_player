from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from . import models
def index(request):
    pass
    return render(request, 'user/index.html')


def login(request):
    if request.method == "POST":  # 通过post请求读取到了用户名和密码
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == '' and password == '':
            message = "请输入用户名和密码！"
            return render(request, 'user/login.html', {"message": message})
        if username and password:
            username = username.strip()
            try:
                current_user = models.User.objects.get(name=username)
                if current_user.password == password:
                    return redirect('/index')  # 正确就重定向到主页，并处于登陆状态
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
            return render(request, 'user/login.html', {"message": message})
    return render(request, 'user/login.html')  # 直接按则没用


def register(request):
    pass
    return render(request, 'user/register.html')


def logout(request):
    pass
    return redirect('/index/')
