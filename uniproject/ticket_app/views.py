from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import login , authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from .models import Ticket
from .forms import TicketForm, NewUserForm

# Here its rendering the index.html view
def index(request):
    return render(request, "index.html")    

# This function checks if the form is valid and if it's being posted
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
            return redirect("index")
        messages.error(request, "Unsuccessful registration. Invalid information")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form":form})

# This function authenticates the username and password to let them login
# This will redirect to idex if authentication is successful
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username , password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("index")
            else:
                messages.error(request, "Invalid username or password")
        else:
                messages.error(request, "Invalid username or password")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html" , context={"login_form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("index")
