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


class ProfileChangeForm(forms.ModelForm):
    
    class Meta:
        model = CustomUser
        fields = '__all__'






# widgetTextInput = forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 'type' : 'text'})
# widgetEmailInput = forms.EmailInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 'type' : 'email'})
# widgetPasswordInput = forms.PasswordInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 'type' : 'password'})
