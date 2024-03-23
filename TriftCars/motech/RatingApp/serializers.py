from rest_framework import serializers 
from .models import RatingModel

class Rating_serializer(serializers.ModelSerializer):
    class Meta:
        model = RatingModel
        fields = '__all__'