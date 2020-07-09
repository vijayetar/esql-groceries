from django.urls import path
from .views import GroceryList, GroceryDetail

urlpatterns = [
  path('', GroceryList.as_view(), name='grocery_list'),
  path('<int:pk>/', GroceryDetail.as_view(), name='grocery_detail'),
]