from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from . import models
from . import forms


def index(request):
    pass
    return render(request, 'user/index.html')


def login(request):
    if request.session.get('is_login', default=None):
        return redirect('/index')
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
                    request.session['is_login'] = True
                    request.session['user_name'] = current_user.name
                    request.session['user_password'] = current_user.password
                    return redirect('/index')  # 正确就重定向到主页，并处于登陆状态
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
            return render(request, 'user/login.html', locals())
        return render(request, 'user/login.html', locals())


def register(request):
    pass
    return render(request, 'user/register.html')


def logout(request):
    request.session.flush()  # 只要登出就把Session全部清空，下面的写法是错误的
    # if request.session.get('is_login', None):
    #     return redirect('/index')
    return redirect('/index')
