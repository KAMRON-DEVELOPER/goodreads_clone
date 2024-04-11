from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View
from users.models import CustomUser
from .forms import UserChangeForm, UserCreationForm, RegisterForm, LoginForm
from django.contrib.auth import login, authenticate, logout


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'users/register.html', {'form' : form})
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user = CustomUser.objects.create(username=username, email=email)
            user.set_password(password)
            user.save()
            
        print(request.user)
        
        # username = request.POST['username']
        # email = request.POST['email']
        # password = request.POST['password']
        # user = CustomUser.objects.create(username=username, email=email)
        # user.set_password(password)
        # user.save()
        
        return redirect('register')
    

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'users/login.html', {'form' : form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('list')
            else:
                return redirect('login')
        else:
            return redirect('login')
        

class DashboardView(View):
    def get(self, request):
        form = LoginForm()
        
        
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('list')