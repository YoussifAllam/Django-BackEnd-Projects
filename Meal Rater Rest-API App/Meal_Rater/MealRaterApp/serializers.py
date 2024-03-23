from  rest_framework import serializers
from .models import Meal_Info ,Meals_Rating

class Meal_Info_serilizer(serializers.ModelSerializer):
    class Meta:
        model = Meal_Info
        fields = '__all__'
        
class Rating_serilizer(serializers.ModelSerializer):
    class Meta:
        model = Meals_Rating
        fields = '__all__'