from django.contrib import admin
from django.urls import path , include
from rest_framework import routers
# from django.conf.urls import include
from .views import Meal_view_set , Rating_view_set 
 

from rest_framework.authentication import BasicAuthentication , TokenAuthentication 

from rest_framework.permissions import IsAuthenticated 

from rest_framework.authtoken.views import obtain_auth_token 

   

 
router = routers.DefaultRouter()
router.register('meals', Meal_view_set)
router.register('rating', Rating_view_set)

urlpatterns = [
    path('', include(router.urls)),
    # path('Rete_Meal', Meal_view_set.Rete_Meal, name='Rete_Meal'),
    path('get-auth-token' , obtain_auth_token  ) ,
]