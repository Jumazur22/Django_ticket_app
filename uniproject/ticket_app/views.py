from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib import messages

from .models import Ticket
from .forms import TicketForm, NewUserForm

# Here its rendering the index.html view
def index(request):
    return render(request, "index.html")    

# This function checks if the form is valid and if its posted
# if so then the form gets saved to the database
def create_ticket(request):
    form = TicketForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TicketForm()

    context = {
        'form' : form
    }
    return render(request, "create_ticket.html", context)

# This function checks if the form is being posted and if its valid
# If so the info is saved and a user is created  and redirected to the homepage
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user =form.save()
            login(request, user)#
            messages.success(request, "Registration successful")
            return redirect("ticket_app:homepage")
        messages.error(request, "Unsuccessful registration. Invalid information")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form":form})