"""
URL configuration for LITRevu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from LITReview.views import (RegistrationView, HomeView, CreateTicketView, UpdateTicketView, PostsView,
                             CreateReviewView, CreateTicketAndReviewView, UpdateReviewView, ReviewDelete, TicketDelete)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('home', HomeView.as_view(), name='home'),
    path('posts', PostsView.as_view(), name='posts'),
    path('ticket_and_review/create_ticket/', CreateTicketView.as_view(), name='ticket_create'),
    path('ticket_and_review/<int:pk>/update_ticket/', UpdateTicketView.as_view(), name='ticket_update'),
    path('ticket_and_review/<int:pk>/update_review/', UpdateReviewView.as_view(), name='review_update'),
    path('ticket_and_review/<int:ticket_id>/create_review', CreateReviewView.as_view(), name='review_create'),
    path('review/<int:pk>/delete/', ReviewDelete.as_view(), name='review_delete'),
    path('ticket/<int:pk>/delete/', TicketDelete.as_view(), name='ticket_delete'),
    path('ticket_and_review/create_ticket_and_review/', CreateTicketAndReviewView.as_view(),
         name='ticket_and_review_create'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
