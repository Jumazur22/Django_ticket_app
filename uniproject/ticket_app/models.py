from django.db import models
from django.db.models import CharField

class Ticket(models.Model):
    issue_type = CharField(("Area of Problem"), max_length=50)
    issue_description = models.TextField(max_length=300)
    date = models.DateTimeField()