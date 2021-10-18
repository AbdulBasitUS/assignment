from django.db import models


class PizzaType(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    type_name = models.CharField(max_length=30)

class PizzaSize(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    size_name = models.CharField(max_length=30)

class PizzaTopping(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    topping_name = models.CharField(max_length=50)