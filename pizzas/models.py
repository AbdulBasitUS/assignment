from django.db import models

# Create your models here.

class PizzaType(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    type_name = models.CharField(max_length=30)