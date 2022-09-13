from django.contrib.auth.models import User
from django.db import models
from django.db.models import CharField

class Ticket(models.Model):
    user = models.ForeignKey(User, default=None , on_delete=models.CASCADE)
    issue_type = CharField(("Area of Problem"), max_length=50)
    issue_description = models.TextField(max_length=300)
    date = models.DateTimeField()