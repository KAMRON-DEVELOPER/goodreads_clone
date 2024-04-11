from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import CustomUser


class RegisterModelForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')
        
    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user


class RegisterForm(forms.Form):
    username = forms.CharField(label="username", max_length=40)
    email = forms.EmailField(label='email', max_length=55)
    password = forms.CharField(label='password', max_length=16)
    
    def save(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        email = self.cleaned_data['email']
        user = CustomUser.objects.create(username=username, email=email)
        user.set_password(password)
        user.save()
        
        return user
        

class LoginForm(forms.Form):
    username = forms.CharField(label="username", max_length=40)
    # email = forms.EmailField(label='email', max_length=55)
    password = forms.CharField(label='password', max_length=16)


class ProfileChangeModelForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'gender', 'employment', 'date_of_birth', 'picture']

    # def save(self, commit=True):
    #     user = super(ProfileChangeModelForm, self).save(commit=False)
    #     password = self.cleaned_data.get('password')

    #     if password:
    #         user.set_password(password)

    #     if commit:
    #         user.save()

    #     return user





# widgetTextInput = forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 'type' : 'text'})
# widgetEmailInput = forms.EmailInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 'type' : 'email'})
# widgetPasswordInput = forms.PasswordInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 'type' : 'password'})
