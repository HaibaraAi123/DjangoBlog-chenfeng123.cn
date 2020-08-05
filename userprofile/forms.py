from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserLoginForm(forms.Form):
    '''
    用户登录表单
    '''
    username = forms.CharField()
    password = forms.CharField()


class UserRegisterForm(forms.ModelForm):
    '''
    注册用户表单
    '''
    password = forms.CharField()
    password_again = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email')

    def CheckPassword(self):
        data = self.cleaned_data
        if data.get('password') == data.get('password_again'):
            return data.get('password')
        else:
            raise forms.ValidationError("两次密码输入不一致，请重试。")


class UserProfileForm(forms.ModelForm):
    '''
    用户详细信息表单
    '''
    class Meta:
        model = Profile
        fields = ('phonenum', 'avatar', 'bio')