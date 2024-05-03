from django.urls import path 
from .views import *
urlpatterns = [
    path('Generate_Text_with_Gemini/' , Generate_Text_wiht_Gemini)
]