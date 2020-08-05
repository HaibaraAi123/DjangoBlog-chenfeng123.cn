from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserLoginForm, UserRegisterForm, UserProfileForm
from .models import Profile


# Create your views here.
def UserLogin(request):
    if request.method == 'POST':
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            # 若数据合法 则使用 .cleaned_data 清洗合法数据
            data = user_login_form.cleaned_data
            # 使用 authenticate 检查账号密码是否匹配数据库中的用户
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                # 保存session 实现登录操作
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("账号密码输入有错误。请重新输入")
        else:
            return HttpResponse("账号或密码输入不合法")
    elif request.method == 'GET':
        user_login_form = UserLoginForm()
        context = {'form': user_login_form}
        return render(request, 'userprofile/login.html', context)
    else:
        return HttpResponse("使用Get或Post方法请求数据")


# 退出登录视图
def UserLogout(request):
    logout(request)
    return HttpResponseRedirect('/')


# 用户注册
def UserRegister(request):
    if request.method == 'POST':
        user_register_form = UserRegisterForm(data=request.POST)
        if user_register_form.is_valid():
            new_user = user_register_form.save(commit=False)
            new_user.set_password(user_register_form.cleaned_data['password'])
            new_user.save()
            login(request, new_user)
            return HttpResponseRedirect(request.path)
    elif request.method == 'GET':
        user_register_form = UserRegisterForm()
        context = {'form': user_register_form}
        return render(request, 'userprofile/register.html', context)
    else:
        return HttpResponse('请使用Get或Post请求数据。')


# 编辑用户信息
@login_required(login_url='/userprofile/login/')
def UserProfileEdit(request, id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user_id=id)

    if request.method == 'POST':
        if request.user != user:
            return HttpResponse("你没有权限修改此用户信息")
        profile_form = UserProfileForm(request.POST, request.FILES)
        #profile_form = UserProfileForm(data=request.POST)
        if profile_form.is_valid():
            profile_cd = profile_form.cleaned_data
            profile.phonenum = profile_cd['phonenum']
            profile.bio = profile_cd['bio']
            if 'avatar' in request.FILES:
                profile.avatar = profile_cd['avatar']
            profile.save()
            # redirect("userprofile:edit", id=id)
            return HttpResponseRedirect(request.path)
        else:
            return HttpResponse("注册表单输入有误。请重新输入。")
    elif request.method == 'GET':
        profile_form = UserProfileForm()
        context = {'profile_form': profile_form, 'profile': profile, 'user': user}
        return render(request, 'userprofile/edit.html', context)
    else:
        return HttpResponse("only post or get method of request")
