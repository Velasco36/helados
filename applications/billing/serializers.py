from rest_framework import serializers
from .models import *



class InvoiceSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = "__all__"
        
