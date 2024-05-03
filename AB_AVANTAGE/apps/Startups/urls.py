from django.urls import path
from .views import GET_ALL_Startups , Add_new_startup

urlpatterns = [
    path('Get_ALL_startups/', GET_ALL_Startups, name='startup-list-create'),
    path('Add_new_startup/' , Add_new_startup)
]
