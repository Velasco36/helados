from django.db import models

# Create your models here.


class Client(models.Model):
    rif = models.CharField(max_lenght=30)
    name: models.CharField(max_lenght=50)
    last_name = models.CharField(max_lenght=50)
    address = models.CharField(max_lenght=100)
    balnce = models.FloatField()

class AccoutnReceivable(models.Model):
    client: models.ForeignKey(Client, on_delete= models.CASCADE)
    amount = models.IntegerField()
