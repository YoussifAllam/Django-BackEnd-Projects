from django.urls import path , include
from . import  views

urlpatterns = [

    # Get All Cars
    # path('get_all_cars_viewset/', include(router.urls)),

    # GET Car using its name
    path('Get_all_Sponsors/', views.Get_all_Sponsors, name='Get_all_Sponsors'),


] 
