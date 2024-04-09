from django.forms import Form, ModelForm
from users.models import CustomUser


class RegisterForm(ModelForm):
    
    class Meta:
        model = CustomUser
        
