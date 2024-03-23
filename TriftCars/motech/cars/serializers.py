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
        fields = ['car_code','Make' , 'Car_model_name' , 'price' , 'status','production_year' , 'mileage' 
                  , 'Car_Color' , 'engine_capacity' , 'Drive' , 'Cylinders_type' , 'Transmission' ,'Fuel_Type'
                  ,'Body_styel' , 'description' , 'photos']




    def get_photos(self, obj):
        request = self.context.get('request')
        return [request.build_absolute_uri(photo.photo.url) for photo in obj.photos.all()]
    
    

class Vistors_serializer(serializers.ModelSerializer):
    class Meta:
        model = num_of_vistors
        fields = "__all__"
    
