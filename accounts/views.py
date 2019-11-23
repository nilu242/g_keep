from django.shortcuts import render
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.shortcuts import redirect


# Create your views here.
class SignUpView(CreateView):
    model = User
    template_name = "accounts/signup.html"
    fields = ['username', 'password', 'first_name', 'last_name', 'email']
    success_url = '/'