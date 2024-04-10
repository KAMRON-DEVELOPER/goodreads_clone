from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')


widgetTextInput = forms.TextInput(attrs={'class': 'appearance-none border rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'})
widgetEmailInput = forms.EmailInput(attrs={'class': 'appearance-none border rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'})
widgetPasswordInput = forms.PasswordInput(attrs={'class': 'appearance-none border rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'})

class RegisterForm(forms.Form):
    username = forms.CharField(label="username", max_length=40, widget=widgetTextInput)
    email = forms.EmailField(label='email', max_length=55, widget=widgetEmailInput)
    password = forms.CharField(label='password', max_length=16, widget=widgetPasswordInput)
        
