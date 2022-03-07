from django.shortcuts import render, HttpResponse
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.

class Login_View(LoginView):
    template_name= 'app_store/home.html'


class Logout_View(LogoutView):
    template_name='app_store/logout.html'