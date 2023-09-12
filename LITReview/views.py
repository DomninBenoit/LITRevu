from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from itertools import chain
from LITReview.forms import TicketAndReviewForm
from LITReview.models import Ticket, Review, UserFollows


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'


class RegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class HomeView(LoginRequiredMixin, ListView):
    template_name = 'body/home.html'

    def get_queryset(self):
        user_tickets = Ticket.objects.filter(user=self.request.user)
        user_reviews = Review.objects.filter(user=self.request.user)

        combined_list = sorted(
            chain(user_tickets, user_reviews),
            key=lambda instance: instance.time_created,
            reverse=True  # Pour trier du plus récent au plus ancien
        )
        return combined_list


class PostsView(LoginRequiredMixin, ListView):
    template_name = 'body/posts.html'

    def get_queryset(self):
        user_tickets = Ticket.objects.filter(user=self.request.user)
        user_reviews = Review.objects.filter(user=self.request.user)

        combined_list = sorted(
            chain(user_tickets, user_reviews),
            key=lambda instance: instance.time_created,
            reverse=True  # Pour trier du plus récent au plus ancien
        )
        return combined_list


class CreateTicketView(CreateView):
    model = Ticket
    fields = ['title', 'description', 'image']
    template_name = 'ticket_and_review/ticket_create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.image = self.request.FILES.get('image')
        return super().form_valid(form)


class UpdateTicketView(UpdateView):
    model = Ticket
    fields = ['title', 'description', 'image']
    template_name = 'ticket_and_review/ticket_update.html'
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.image = self.request.FILES.get('image')
        return super().form_valid(form)


class TicketDelete(DeleteView):
    model = Ticket
    template_name = 'ticket_and_review/confirm_delete.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return Ticket.objects.filter(user=self.request.user)


class CreateReviewView(CreateView):
    model = Review
    fields = ['headline', 'rating', 'body']
    template_name = 'ticket_and_review/review_create.html'
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


class UpdateReviewView(UpdateView):
    model = Review
    fields = ['headline', 'rating', 'body']
    template_name = 'ticket_and_review/review_create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ReviewDelete(DeleteView):
    model = Review
    template_name = 'ticket_and_review/confirm_delete.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)


class CreateTicketAndReviewView(CreateView):
    model = Ticket
    template_name = 'ticket_and_review/ticket_and_review_create.html'
    form_class = TicketAndReviewForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # D'abord sauver le ticket
        ticket = Ticket(
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'],
            user=self.request.user,
            image=self.request.FILES.get('image')
        )
        ticket.save()
        self.object = ticket

        # Ensuite, sauver la review
        review = Review(
            ticket=ticket,
            headline=form.cleaned_data['headline'],
            rating=form.cleaned_data['rating'],
            body=form.cleaned_data['body'],
            user=self.request.user
        )
        review.save()

        return redirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class FollowView(TemplateView):
    template_name = 'body/follows.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        search_query = self.request.GET.get('search', '')
        context['users'] = []
        if search_query:
            context['users'] = User.objects.filter(username__icontains=search_query)

        followed_users = self.request.user.followed.values_list('followed_user', flat=True)
        context['followed_users_list'] = User.objects.filter(pk__in=followed_users)

        followers = UserFollows.objects.filter(followed_user=self.request.user).values_list('user', flat=True)
        context['followers_list'] = User.objects.filter(id__in=followers)

        context['search_query'] = search_query
        return context

    def post(self, request):
        # Désabonner
        user_id_to_unfollow = request.POST.get('unfollow_user_id')
        if user_id_to_unfollow:
            try:
                user_to_unfollow = User.objects.get(pk=user_id_to_unfollow)
                unfollow_relation = UserFollows.objects.get(user=request.user, followed_user=user_to_unfollow)
                unfollow_relation.delete()
                return redirect(request.path)
            except (User.DoesNotExist, UserFollows.DoesNotExist):
                pass

        # S'abonner
        user_id_to_follow = request.POST.get('follow_user_id')
        if user_id_to_follow:
            try:
                user_to_follow = User.objects.get(pk=user_id_to_follow)
                if not UserFollows.objects.filter(user=request.user, followed_user=user_to_follow).exists():
                    UserFollows.objects.create(user=request.user, followed_user=user_to_follow)
                return redirect(request.path)
            except User.DoesNotExist:
                pass

        return redirect(request.path)


