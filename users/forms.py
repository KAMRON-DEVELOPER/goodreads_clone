from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')


class RegisterForm(forms.Form):
    username = forms.CharField(label="username", max_length=40)
    email = forms.EmailField(label='email', max_length=55)
    password = forms.CharField(label='password', max_length=16)
        
