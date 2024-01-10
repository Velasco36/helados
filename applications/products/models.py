from django.db import models

class Classification(models.Model):

    name = models.CharField(max_length=50)

class Paleta(models.Model):

    classification = models.ForeignKey(Classification, on_delete=models.CASCADE)

    name = models.CharField(max_length=50)

    description = models.TextField()

    price = models.FloatField()

class RawMaterialInventory(models.Model):

    name = models.CharField(max_length=50)

class MerchandiseMovement(models.Model):

    inventory = models.ForeignKey(RawMaterialInventory, on_delete=models.CASCADE)

    initial_inventory = models.IntegerField()

    final_inventory = models.IntegerField()

    movement_date = models.DateTimeField()

class PaletaInventory(models.Model):

    paleta = models.ForeignKey(Paleta, on_delete=models.CASCADE)

    quantity = models.IntegerField()
