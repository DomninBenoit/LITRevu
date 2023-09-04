from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from LITReview.models import Ticket, Review


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
    fields = ['title', 'description', 'image']
    template_name = 'ticket/ticket_create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.image = self.request.FILES.get('image')
        return super().form_valid(form)


class UpdateTicketView(UpdateView):
    model = Ticket
    fields = ['title', 'description', 'image']
    template_name = 'ticket/ticket_update.html'
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.image = self.request.FILES.get('image')
        return super().form_valid(form)


class CreateReviewView(CreateView):
    model = Review
    fields = ['headline', 'rating', 'body']
    template_name = 'review/review_create.html'
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        self.ticket = Ticket.objects.get(pk=self.kwargs["ticket_id"])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ticket'] = self.ticket
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.ticket = self.ticket
        return super().form_valid(form)