from django import forms
from .models import Ticket


class TicketAndReviewForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']

    headline = forms.CharField(max_length=128)
    rating = forms.ChoiceField(choices=[(i, i) for i in range(6)])
    body = forms.CharField(widget=forms.Textarea, max_length=8192)

