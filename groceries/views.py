from django.shortcuts import render
from rest_framework import generics

from .models import Grocery
from .serializers import GrocerySerializer
# Create your views here.
class GroceryList(generics.ListCreateAPIView):
  queryset = Grocery.objects.all()
  serializer_class = GrocerySerializer

class GroceryDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset=Grocery.objects.all()
  serializer_class = GrocerySerializer