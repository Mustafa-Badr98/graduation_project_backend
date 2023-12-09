from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import NewUser
from .forms import NewUserForm

from django.contrib.auth.views import LoginView
from .forms import UserLoginForm



class UserCreateView(CreateView):
    model = NewUser
    form_class = NewUserForm
    template_name = 'registration/user_create.html'  # Create this template with your form rendering
    # success_url = reverse_lazy('home')  # Replace 'success-url' with your actual success URL
    success_url='login/'


class SuperuserCreateView(CreateView):
    model = NewUser
    form_class = NewUserForm
    template_name = 'superuser_create.html'  # Create this template with your form rendering
    success_url = reverse_lazy('success-url')  # Replace 'success-url' with your actual success URL

    def form_valid(self, form):
        form.instance.is_staff = True
        form.instance.is_superuser = True
        return super().form_valid(form)
    

class UserLoginView(LoginView):
    template_name = 'registration/login.html'  # Create this template with your login form rendering
    form_class = UserLoginForm
    success_url=reverse_lazy('home')
    