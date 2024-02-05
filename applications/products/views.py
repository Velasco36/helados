from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *


class ClassificationViewSet(viewsets.ModelViewSet):
    queryset= Classification.objects.all()
    serializer_class = ClassificationSeralizer


class PaletaViewSet(viewsets.ModelViewSet):
    queryset = Paleta.objects.all()
    serializer_class = PaletaSerialzers

class RawMaterialInventoryView(viewsets.ModelViewSet):
    queryset = RawMaterialInventory.objects.all()
    serializer_class = RawMaterialInventorySerialzer

class MerchandiseMovementView(viewsets.ModelViewSet):
    queryset = MerchandiseMovement.objects.all()
    serializer_class = MerchandiseMovement
class PaletaInventoryView(viewsets.ModelViewSet):
    queryset = PaletaInventory
    serializer_class = PaletaInventorySerializers
# Create your views here.
