from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from LITReview.forms import TicketForm
from LITReview.models import Ticket


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'


class RegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class HomeView(TemplateView):
    template_name = 'body/home.html'


class PostsView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'body/posts.html'

    def get_queryset(self):
        return Ticket.objects.filter(user=self.request.user)


class CreateTicketView(CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'ticket/ticket_create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateTicketView(UpdateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'ticket/ticket_update.html'
    success_url = reverse_lazy('posts')
