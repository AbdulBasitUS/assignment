from rest_framework import serializers
from .models import PizzaType

class PizzaTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaType
        fields = '__all__'