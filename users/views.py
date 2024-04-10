from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View
from .forms import UserChangeForm, UserCreationForm, RegisterForm


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'users/register.html', {'form' : form})
    
    def post(self, request):
        # form = RegisterForm(request.POST)
        # if form.is_valid():
        #     username = form.cleaned_data['username']
        #     password = form.cleaned_data['password']
        #     email = form.cleaned_data['email']
            
        # print(username)
        print(request.POST['full_name'])
        return redirect('register')
    

def login(request):
    return render(request, 'users/login.html')