from django import forms
from  django.contrib.auth.forms import AuthenticationForm
import  re
from users.models import UserLog,UserProfile
class LoginForm(forms.Form):
    # username = forms.CharField(
    #     # label='用户名',
    #     max_length=20,
    # )
    # password = forms.CharField(
    #     # label='密码',
    #     # widget=forms.PasswordInput,
    #     max_length=20,
    # )
    username = forms.CharField(required=True, label="用户名", error_messages={'required': '你的账号不能为空'},
                               widget=forms.TextInput(attrs={'class':'form-control','placeholder': u"请输入用户名"}))
    password = forms.CharField(required=True, label="密码", error_messages={'required': '请输入你的密码'},
                               widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': "请输入密码"}))



class UserCreateForm(forms.ModelForm):

    username = forms.CharField(required=True, label="用户名:",
                               error_messages={'required': '用户名不能为空'},
                               max_length=15,help_text='*必填',
                               widget=forms.TextInput(attrs={'class':'form-control','placeholder': u"用户名"}))

    nick_name = forms.CharField(label="昵称;",help_text='可不填',
                                widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'昵称'}))

    password = forms.CharField(required=True, label="密码:",
                               error_messages={'required': '密码不能为空',},
                               max_length=20,help_text='*必填',
                               widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': "密码"}))

    mobile = forms.CharField(required=True,label="手机号:",
                             error_messages={'required': '手机号不能为空'},
                             max_length=11,help_text='*必填',
                             widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'手机号'}))
    #
    email = forms.EmailField(required=True,label='邮箱:',
                             error_messages={'required': '邮箱不能为空'},help_text='*必填',
                             widget=forms.EmailInput(attrs={'class':'form-control','placeholder': u"邮箱"}))
    # username = forms.CharField()
    class Meta:
        model = UserProfile
        fields = ['username','nick_name','password','email','mobile']
        # error_messages ={
        #     'username':'用户名不能为空',
        #     'password':'密码不能为空',
        #     'email':'邮箱不能为空',
        #     'mobile':'手机号不能为空',
        # }
        # help_texts = {
        #     'username':'*必填',
        #     'password':'*必填',
        #     'email':'*必填',
        #     'mobile':'*必填',
        # }
        # widgets ={
        #     'password':forms.PasswordInput(attrs={'class': 'form-control','placeholder':'密码'})
        # }

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError("手机号码非法", code="mobile_invalid")


class UserUpdateModelForm(forms.ModelForm):
    '''用户资料更新'''
    class Meta:
        model = UserProfile
        fields = ['nick_name','username','email','mobile',]
        # exclude = ['password','user_permissions']
        labels = {
            'username':'用户名',
            'nick_name':'昵称'
        }
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'nick_name':forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            # 'is_superuser': forms.Select(),
            # 'is_active': forms.CheckboxInput(attrs={'class': 'form-control'}),
            # 'is_staff': forms.CheckboxInput(attrs={'class': 'form-control'}),

        }
class UpdatePasswordForm(forms.Form):
    '''修改密码'''
    # old_password = forms.CharField(
    #     widget=forms.PasswordInput,
    #     min_length=5,
    #     max_length=20,
    #     help_text='*必填',
    #     error_messages='密码不能为空',
    #     label='旧密码:',
    # )
    # new_password = forms.CharField(
    #     widget=forms.PasswordInput,
    #     min_length=5,
    #     max_length=20,
    #     help_text='*必填',
    #     error_messages='密码不能为空',
    #     label='新密码:',
    # )
    # confirm_password = forms.CharField(
    #     widget=forms.PasswordInput,
    #     min_length=5,
    #     max_length=20,
    #     help_text='*必填',
    #     error_messages='密码不能为空',
    #     label='确认密码:',
    # )

    # )
    old_password = forms.CharField(
        max_length=128, widget=forms.PasswordInput,label='旧密码')
    new_password = forms.CharField(
        min_length=5, max_length=128, widget=forms.PasswordInput,label='新密码',help_text="* 最少为5个字符")
    confirm_password = forms.CharField(
        min_length=5, max_length=128, widget=forms.PasswordInput,label='确认密码',help_text="* 最少为5个字符")
