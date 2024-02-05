from rest_framework import serializers
from .models import *

class ClassificationSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Classification
        fields = "__all__"

class PaletaSerialzers(serializers.ModelSerializer):
    class Meta:
        model= Paleta
        fields = "__all__"

class RawMaterialInventorySerialzer(serializers.ModelSerializer):
    class Meta:
        model = RawMaterialInventory
        fields= "__all__"

class MerchandiseMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = MerchandiseMovement
        fields = "__all__"

class PaletaInventorySerializers(serializers.ModelSerializer):
    class Meta:
        model= PaletaInventory
        fields= "__all__"

