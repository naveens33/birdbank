from django.db import models
# Create your models here.
from django.contrib.auth.models import User


class Account(models.Model):
    UserId = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    AccountNumber = models.CharField(max_length=30, primary_key=True)
    Branch = models.CharField(max_length=30)
    Type = models.CharField(max_length=30)
    Balance = models.FloatField()
    IFSCCode = models.CharField(max_length=30)
