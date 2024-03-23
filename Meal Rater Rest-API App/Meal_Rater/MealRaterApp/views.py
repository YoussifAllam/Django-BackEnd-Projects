from django.shortcuts import render
from rest_framework import viewsets  , status
from .models import Meal_Info , Meals_Rating 
from .serializers import Rating_serilizer , Meal_Info_serilizer
from django.contrib.auth.models import User
from rest_framework.decorators import action 
from rest_framework.response import Response
from rest_framework.authentication import   TokenAuthentication
from rest_framework.permissions import AllowAny , IsAuthenticated , IsAdminUser , IsAuthenticatedOrReadOnly
# Create your views here.

class Meal_view_set(viewsets.ModelViewSet): 
    queryset  =Meal_Info.objects.all()
    serializer_class = Meal_Info_serilizer
    authentication_classes = [TokenAuthentication  ]
    permission_classes = [IsAuthenticated]  
    
    @action(methods = ['POST'] ,detail = True)
    def  Rete_Meal(self , Request ):
        if 'stars' in Request.data : 
            pk  = Request.Get.get('pk')
            Targer_Meal  = Meal_Info.objects.get( id = pk)
            # Target_User_name  = Request.data['username']
            Target_User = Request.user
            Rating_stars = Request.data['stars']
            #   Target_User = User.objects.get(username = Target_User_name)
            
            try: # if there is old rate and we will update it
                # get old rating
                Rate = Meals_Rating.objects.get(
                    Target_User = Target_User.id ,
                    Targer_Meal = Targer_Meal.id
                )
                
                Meals_Rating.Rating_stars = Rating_stars
                Meals_Rating.save()
                serializer = Rating_serilizer(Meals_Rating , many = False)
                json = {
                    'message' : 'Updated',
                    'resualt' : serializer.data
                }
                
                return Response(json ,status= status.HTTP_400_bad_request) 
                
            except: # if this is the first time to rate this meal using this user
                rating   = Meals_Rating.objects.create(
                    Target_User  = Target_User.id ,
                    Rating_stars = Rating_stars   ,
                    Targer_Meal  = Targer_Meal )
                
                serializer = Rating_serilizer(rating , many = False)
                
                json = {
                    'message' : 'Created',
                    'resualt' : serializer.data
                }
                return Response(json ,status= status.HTTP_200_OK)
        else : 
            json = {
                    'message' : 'Updated',
                    'resualt' : serializer.data
                }
                
            return Response(json ,status= status.HTTP_400_bad_request) 
        
    
class Rating_view_set(viewsets.ModelViewSet):
    queryset = Meals_Rating.objects.all()
    serializer_class = Rating_serilizer
    authentication_classes = [TokenAuthentication  ]
    permission_classes = [IsAuthenticated]  