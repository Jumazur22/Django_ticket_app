from django import forms

from .models import Ticket

class TicketForm(forms.ModelForm):
    date = forms.DateTimeField(
        label = 'Date & Time',
        widget = forms.widgets.DateTimeInput(attrs={'type':'datetime-local'}),
    )
    issue_type = forms.CharField(
        widget = forms.widgets.Input(attrs={'style':'border-color:lightblue'}),
    )
    issue_description = forms.CharField(
        widget = forms.widgets.Textarea(attrs={'style':'border-color:lightblue'}),
    )
    class Meta:
        model = Ticket
        fields = [
            'issue_type' ,
            'issue_description',
            'date'
        ]