from rest_framework import serializers
from .models import PDF

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDF
        fields = '__all__'
