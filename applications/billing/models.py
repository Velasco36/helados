from django.db import models

from applications.products.models import Paleta
from applications.accounts.models import Client


# Create your models here.
class Invoice(models.Model):
    date = models.DateTimeField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    paleta = models.ForeignKey(Paleta, on_delete= models.CASCADE)
    unit_price = models.IntegerField()
    quantity = models.IntegerField()
    type = models.IntegerField() #modificar devolusion o recibo
    amount = models.IntegerField()
    debt = models.IntegerField()
    payment = models.IntegerField()
    total = models.IntegerField()

