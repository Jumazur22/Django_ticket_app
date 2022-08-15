from django.shortcuts import render
from django.http import HttpResponse

from .models import Ticket
from .forms import TicketForm

# Here its rendering the index.html view
def index(request):
    return render(request, "index.html")    

# This function sets the form variable for the TicketForm
# and checks if the form is valid and if it is then it gets saved to the datbase
def create_ticket(request):
    form = TicketForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TicketForm()

    context = {
        'form' : form
    }
    return render(request, "create_ticket.html", context)
    