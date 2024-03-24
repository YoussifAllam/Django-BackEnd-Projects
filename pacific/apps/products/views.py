from django.shortcuts import render, redirect
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
# from rest_framework.views import APIView
from django.http import  Http404


@method_decorator(never_cache, name='dispatch')
class View_get_all_Category1(viewsets.ModelViewSet):
    queryset = Category1.objects.all()
    serializer_class = Category_1_Serializer

    def list(self, request, *args, **kwargs):
        response = super(View_get_all_Category1, self).list(request, *args, **kwargs)
        formatted_response = {
            "status": "success",
            "data": {
                "Products": response.data
            }
        }

        return Response(formatted_response , status=status.HTTP_200_OK)
    

@api_view(['GET'])
def get_products_in_category2(request):
    Category1_name = request.GET.get('Category1_name')
    if Category1_name:
        try:
            category2_objects = Category2.objects.filter(Main_category_fk__Title=Category1_name)
            serializer = Category_2_Serializer(category2_objects, many=True ,  context={'request': request})
            json = {
                "status": "success",
                "data": {
                    "Products": serializer.data
                }
            }
            return Response(json)
        except ObjectDoesNotExist:
            return Response({"message": "Category with the specified title does not exist."}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({"message": "You should enter Category1_name."}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_products_in_category3(request):
    Category2_name = request.GET.get('Category2_name')
    if Category2_name:
        try:
            category2_objects = Category3.objects.filter(category2_fk__Product_Name=Category2_name)
            serializer = Category_3_Serializer(category2_objects, many=True ,  context={'request': request})
            json = {
                "status": "success",
                "data": {
                    "Products": serializer.data
                }
            }
            return Response(json)
        except ObjectDoesNotExist:
            return Response({"message": "Category with the specified title does not exist."}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({"message": "You should enter Category2_name."}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def get_category3_coverIamge(request):
    # Category2_name = request.GET.get('Category2_name')
        try:
            category2_objects = Category3_coverIamge.objects.filter(category3_fk__id=1)
            serializer = Category_3_CoverImage_Serializer(category2_objects, many=True ,  context={'request': request})
            json = {
                "status": "success",
                "data": {
                    "image": serializer.data
                }
            }
            return Response(json)
        except ObjectDoesNotExist:
            return Response({"message": "Category with the specified title does not exist."}, status=status.HTTP_404_NOT_FOUND)