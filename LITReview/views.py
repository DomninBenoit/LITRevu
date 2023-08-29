from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'


class RegistrationView(CreateView):
    form_class = UserCreationForm  # Utilisez le formulaire d'inscription par défaut de Django
    template_name = 'registration/register.html'  # Chemin vers le template d'enregistrement
    success_url = reverse_lazy('login')  # Rediriger vers la page de connexion après l'enregistrement


class HomeView(TemplateView):
    template_name = 'body/home.html'
