from rest_framework import serializers 
from . models import *

class Category_1_Serializer(serializers.ModelSerializer):
    class Meta:
        model  = Category1
        fields = ['Title' , 'Main_image' ,'Cover_image']

class Category2_Serializer(serializers.ModelSerializer):
    class Meta:
        model  = Category2
        fields = ['Product_Name' ,'Cover_image' , 'Cover_image' ]



"""class Benefits_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Benefits_for_Final_Product
        fields = ['Benefit']

class Weights_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Weights_for_Final_Product
        fields = ['Weight']

class grindings_Serializer(serializers.ModelSerializer):
    class Meta:
        model = grinding_for_Final_Product
        fields = ['grinding_Type']
"""

class FinalProductSerializer(serializers.ModelSerializer):
    Benefits = serializers.SerializerMethodField()
    Weights = serializers.SerializerMethodField()
    Grinding_Types = serializers.SerializerMethodField()

    class Meta:
        model  = Final_Product
        fields = ['Product_Name' , 'Product_image' , 'Benefits' , 'Weights' , 'Grinding_Types' ]

    def get_Benefits(self , obj):
        benefits_queryset = Benefits_for_Final_Product.objects.filter(category3_fk=obj.id)
        benefits_list = [benefit.Benefit for benefit in benefits_queryset]
        return benefits_list
    
    def get_Weights(self, obj):
        weights_queryset = Weights_for_Final_Product.objects.filter(category3_fk=obj.id)
        return [weight.Weight for weight in weights_queryset]

    def get_Grinding_Types(self, obj):
        grinding_queryset = grinding_for_Final_Product.objects.filter(category3_fk=obj.id)
        return [grinding.grinding_Type for grinding in grinding_queryset]

    
class FinalProduct_for_C3Serializer(serializers.ModelSerializer):
    Benefits = serializers.SerializerMethodField()
    Weights = serializers.SerializerMethodField()
    Grinding_Types = serializers.SerializerMethodField()

    class Meta:
        model  = Final_Product
        fields = ['Product_Name' , 'Product_image' , 'Benefits' , 'Weights' , 'Grinding_Types' ]

    def get_Benefits(self , obj):
        benefits_queryset = Benefits_for_C3.objects.filter(category3_fk=obj.id)
        benefits_list = [benefit.Benefit for benefit in benefits_queryset]
        return benefits_list
    
    def get_Weights(self, obj):
        weights_queryset = Weights_for_C3.objects.filter(category3_fk=obj.id)
        return [weight.Weight for weight in weights_queryset]

    def get_Grinding_Types(self, obj):
        grinding_queryset = grinding_for_C3.objects.filter(category3_fk=obj.id)
        return [grinding.grinding_Type for grinding in grinding_queryset]

# class Category_2_Serializer(serializers.ModelSerializer):
#     C2 = serializers.SerializerMethodField()
#     # Final_Products = serializers.SerializerMethodField()
#     class Meta:
#         model  = Category1
#         fields = ['C2']

#     def get_C2(self, obj):
#         C2_queryset = obj.objects.all()
#         return Category2_Serializer(C2_queryset , many = True).data
    

# class Category_3_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model  = Category3
#         fields = ['Product_Name' , 'Product_image' ,'Product_Desc'  ]

# class Category_3_CoverImage_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model  = Category3_coverIamge
#         fields = ['Image']