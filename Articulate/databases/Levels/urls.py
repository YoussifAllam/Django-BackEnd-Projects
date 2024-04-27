from django.urls import path , include
# from rest_framework.routers import DefaultRouter
from .views import *

#app name 
# app_name = 'Users'
# router = DefaultRouter()
# router.register(r'users', UserViewSet,basename='users') 

urlpatterns = [
    path('get_sound_in_level1/', get_sound_in_level1, name='get_sound_in_level1'),
    path('get_sound_in_level2/', get_sound_in_level2, name='get_sound_in_level2'),
    path('get_Sentence/', get_sound_in_level3, name='get_Sentence'),
    path('get_all_ReadingTest/', get_all_ReadingTest.as_view({'get': 'list'}), name='get_all_ReadingTest'),
    path('get_lvl_1_sd/', get_lvl_1_sd.as_view({'get': 'list'}), name='get_lvl_1_sd'),
    path('get_lvl_2_sd/', get_lvl_2_sd.as_view({'get': 'list'}), name='get_lvl_2_sd'),
    path('get_lvl_3_sd/', get_lvl_3_sd.as_view({'get': 'list'}), name='get_lvl_3_sd'),
]