from django.shortcuts import render
from django.http import HttpResponse

from .models import Ticket
from .forms import TicketForm

def index(request):
    return render(request, "ticket/index.html")    

def create_ticket(request):
    form = TicketForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TicketForm()

    context = {
        'form' : form
    }
    return render(request, "ticket/create_ticket.html", context)
    