from rest_framework import serializers
from .models import Grocery

class GrocerySerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('name', 'user', 'price')
    model = Grocery