from django.urls import path , include
from . import  views

urlpatterns = [

    # Get All Cars
    # path('get_all_cars_viewset/', include(router.urls)),

    # GET Car using its name
    path('Rating_FBV', views.Rating_FBV, name='Rating_FBV'),


] 
