from rest_framework import serializers
from .models import *


class Clientserializers(serializers.ModelSerializer):
    model = Client
    fields = "__all_"


class AccountsReceivable(serializers.ModelField):
    model = AccountsReceivable
    fields ="__all__"
