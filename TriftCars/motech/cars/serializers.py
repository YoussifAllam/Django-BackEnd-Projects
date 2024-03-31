from rest_framework import serializers 
from .models import Cars_Info, CarPhoto , num_of_vistors

class CarPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPhoto
        fields = ['photo']


class Cars_Serializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField()

    class Meta:
        model = Cars_Info
        fields = ['id','car_code','Make' , 'Car_model_name' , 'price' , 'status','production_year' , 'mileage' 
                  , 'Car_Color' , 'engine_capacity' , 'Drive' , 'Cylinders_type' , 'Transmission' ,'Fuel_Type'
                  ,'Body_styel' , 'description' , 'photos']

class Cars_Update_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Cars_Info
        fields = ['id','car_code','Make' , 'Car_model_name' , 'price' , 'status','production_year' , 'mileage' 
                  , 'Car_Color' , 'engine_capacity' , 'Drive' , 'Cylinders_type' , 'Transmission' ,'Fuel_Type'
                  ,'Body_styel' , 'description' , 'photos']


    ef get_photos(self, obj):
        request = self.context.get('request')
        return [request.build_absolute_uri(photo.photo.url) for photo in obj.photos.all()]d
    

class Vistors_serializer(serializers.ModelSerializer):
    class Meta:
        model = num_of_vistors
        fields = "__all__"
    

class CarPhotoUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPhoto
        fields = ['car', 'photo']
