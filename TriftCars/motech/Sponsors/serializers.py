from rest_framework import serializers
from .models import Sponsors_Model

class Sponsors_serializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsors_Model
        fields = '__all__'