from django.db import models

from applications.products.models import PaletaInventory
from applications.accounts.models import Client

# class Type(models.Model):

#     name = models.CharField(max_length=50)

class Invoice(models.Model):

    date = models.DateField()

    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    paleta = models.ForeignKey(PaletaInventory, on_delete=models.CASCADE)

    unit_price = models.IntegerField()

    quantity = models.IntegerField()

    # type = models.IntegerField() # invoice type

    amount = models.IntegerField()

    debt = models.IntegerField()

    payment = models.IntegerField()

    total = models.IntegerField()
