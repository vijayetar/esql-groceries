from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Grocery(models.Model):
  name = models.CharField(max_length=124)
  user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  price = models.IntegerField(max_length=100)
  def __str__(self):
    return self.name