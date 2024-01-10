from django.db import models

class Client(models.Model):

    name = models.CharField(max_length=50)

    last_name = models.CharField(max_length=50)

    address = models.CharField(max_length=100)

    balance = models.FloatField()

class AccountsReceivable(models.Model):

    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    amount = models.IntegerField()
