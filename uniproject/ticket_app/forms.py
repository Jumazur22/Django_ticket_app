from django import forms
from .models import Ticket

# Django has a pre-build model User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# This is a form to open a case to create a ticket
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

# Here we are creating a user registration form
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2"
        )
    
    # This saves the newly register user details
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user