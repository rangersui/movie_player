from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from . import models
from . import forms
import hashlib


def hash_code(current_string: str, salt='screw'):
    hash_handle = hashlib.sha256()
    current_string += salt
    hash_handle.update(current_string.encode())
    return hash_handle.hexdigest()

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
                if current_user.password == hash_code(password):
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
    if request.session.get('is_login', None):  # 登录状态不允许注册
        return redirect("/index/")
    if request.method == "POST":
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'user/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'user/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'user/register.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = models.User.objects.create()
                new_user.name = username
                new_user.password = hash_code(password1)
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/login/')  # 自动跳转到登录页面
    register_form = forms.RegisterForm()
    return render(request, 'user/register.html', locals())


def logout(request):
    request.session.flush()  # 只要登出就把Session全部清空
    if not request.session.get('is_login', None):  # 没有登录就直接返回主页
        return redirect('/index')
    return redirect('/index')
