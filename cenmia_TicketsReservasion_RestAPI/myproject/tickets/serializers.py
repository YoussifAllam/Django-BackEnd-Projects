from rest_framework import serializers
from tickets.models import Guest , Movie , reservation , Blog


class Guest_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = '__all__'

class reservation_Serializer(serializers.ModelSerializer):
    class Meta:
        model = reservation
        fields = '__all__'
        
class Movie_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['pk' , 'reservation' , 'hall' , 'Movie_name']
        
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'