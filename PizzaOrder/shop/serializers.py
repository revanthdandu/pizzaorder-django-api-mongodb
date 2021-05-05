from rest_framework import serializers
from .models import Topping, Pizza

class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = '__all__'

class PizzaSerializer(serializers.ModelSerializer):
    # pizza_toppings = ToppingSerializer(many=True, required=False)
    class Meta:
        model = Pizza
        fields = '__all__'