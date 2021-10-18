from rest_framework import serializers
from .models import (
    PizzaType,
    PizzaSize,
    PizzaTopping,
    Pizza
)


class PizzaTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaType
        fields = '__all__'

class PizzaSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaSize
        fields = '__all__'

class PizzaToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaTopping
        fields = '__all__'

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = '__all__'
        
    def to_representation(self, instance):
        representation = super(PizzaSerializer, self).to_representation(instance)
        representation['toppings'] = PizzaToppingSerializer(instance.toppings.all(), many=True).data
        representation['type'] = PizzaTypeSerializer(instance.type).data
        representation['size'] = PizzaSizeSerializer(instance.size).data
        return representation