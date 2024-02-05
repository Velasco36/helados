from django.db import models

# Create your models here.
class Clasification(models.Model):
    name = models.CharField(max_lenght=50)

class Paleta(models.Model):
    clasification = models.ForeignKey(Clasification, on_delete=models.CASCADE)
    name = models.CharField(max_lenght=50)
    description = models.TextField()
    price = models.FloatField()

class RawMaterialInventory(models.Model):
    name = models.CharField(max_lenght=50)

class MerchandiseMovement(models.Model):
    inventory = models.Foren(RawMaterialInventory, on_delete=models.CASCADE)
    initial_inventory = models.IntegerField()
    final_inventory = models.IntegerField()
    movement_date = models.DateTimeField()

class PaletaInventory(models.Model):
    paleta = models.ForeignKey(Paleta, on_delete=models.CASCADE)
    quantity = models.IntegerField()
