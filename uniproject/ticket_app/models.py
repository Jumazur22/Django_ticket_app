from django.db import models
from django.db.models import CharField

class Ticket(models.Model):
    issue_type = CharField(("Area of Problem"), max_length=50)
    issue_description = models.TextField(max_length=300)
    date = models.DateTimeField(("Date of when the issue occured"))

    def __str__(self):
        return self.Ticket
    
class User(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    ticket = models.ForeignKey( Ticket, on_delete=models.CASCADE)