from rest_framework import serializers 
from . models import *

class Category_1_Serializer(serializers.ModelSerializer):
    class Meta:
        model  = Category1
        fields = ['Title' , 'Main_image' ,'Cover_image']

class Category_2_Serializer(serializers.ModelSerializer):
    class Meta:
        model  = Category2
        fields = ['Product_Name' , 'Product_image' ,'Product_Desc'  , 'Is_Catogry']

class Category_3_Serializer(serializers.ModelSerializer):
    class Meta:
        model  = Category3
        fields = ['Product_Name' , 'Product_image' ,'Product_Desc'  ]

class Category_3_CoverImage_Serializer(serializers.ModelSerializer):
    class Meta:
        model  = Category3_coverIamge
        fields = ['Image']