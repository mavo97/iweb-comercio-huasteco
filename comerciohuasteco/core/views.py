from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.
class HomePageView(TemplateView):
    template_name = "core/home.html"
class LoginPageView(TemplateView):
    template_name = "core/login.html"
class SignUpPageView(TemplateView):
    template_name = "core/signup.html"
