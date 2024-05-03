from rest_framework import serializers
from .models import StartUp_Model

class StartappsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartUp_Model
        fields = '__all__'
