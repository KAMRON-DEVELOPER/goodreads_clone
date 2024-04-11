from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View
from users.models import CustomUser
from .forms import RegisterModelForm, RegisterForm, LoginForm, ProfileChangeModelForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        formModel = RegisterModelForm()
        return render(request, 'users/register.html', {'form' : form, 'form1' : formModel})
    
    def post(self, request):
        form1 = RegisterForm(request.POST)
        form = RegisterModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return redirect('register', {'form' : form})

    

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
        user = request.user
        form = ProfileChangeModelForm(instance=user)
        return render(request, 'users/profile.html', {'user': user, 'form' : form})
    
    def post(self, request):
        form = ProfileChangeModelForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            print('form is valid')
            form.save()
            messages.success(request, "your data has been changed!")
            return redirect('dashboard')
        else:
            print('form is not valid')
            return render(request, 'users/profile.html', {'form' : form})
        
        
class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.warning(request, "You have lusscessfully logged out!")
        return redirect('list')