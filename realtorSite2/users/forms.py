# forms.py
from django import forms
from users.models import NewUser
from django.contrib.auth.forms import AuthenticationForm

class NewUserForm(forms.ModelForm):
    class Meta:
        model = NewUser
        fields = ['email', 'user_name', 'password', 'first_name', 'last_name', 'profile_pic']
        widgets = {
            'password': forms.PasswordInput(),
        }


class UserLoginForm(AuthenticationForm):
    pass
