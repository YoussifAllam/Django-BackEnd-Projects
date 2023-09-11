from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm


class Creat_user_form(forms.ModelForm):
    username = forms.CharField(label='الاسم ')
    first_name = forms.CharField(label='الاسم الاول')
    last_name = forms.CharField(label=' الاسم الثاني')
    email = forms.EmailField(label='البريد' )
    password1 = forms.CharField(label='كلمه السر',widget= forms.PasswordInput(),min_length= 8)
    password2 = forms.CharField(label='تأكيد كلمه السر',widget= forms.PasswordInput(),min_length= 8)
    
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')


class Login_Form(forms.ModelForm):
    username = forms.CharField(label='الاسم')
    password = forms.CharField(label='البسورد' , widget= forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','password')
        
        
class Update_user_form(forms.ModelForm):
    first_name = forms.CharField(label='الاسم الاول')
    last_name = forms.CharField(label=' الاسم الثاني')
    email = forms.EmailField(label='البريد' )

    class Meta:
        model = User
        fields = ('first_name','last_name','email')