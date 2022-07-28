from django import forms

from .models import Ticket

class TicketForm(forms.ModelForm):
    date = forms.DateTimeField(
        label = 'Date & Time',
        widget = forms.widgets.DateTimeInput(attrs={'type':'datetime-local'}),
    )
    class Meta:
        model = Ticket
        fields = [
            'issue_type',
            'issue_description',
            'date'
        ]