# from django.contrib import admin
from django.urls import path , include
# from django.conf import settings
# from django.conf.urls.static import static
from cars import  views

from rest_framework.routers import DefaultRouter
#  from rest_framework.authtoken.views import obtain_auth_token
router = DefaultRouter()
router.register('Cars', views.viewsets_GetAllCars)
router.register('Vistors', views.Num_of_vistors)

urlpatterns = [

    # Get All Cars
    path('get_all_cars_viewset/', include(router.urls)),

    # GET Car using its name
    path('get_car_by_name', views.get_car_by_name, name='get_car_by_name'),

    path('Add-Car/' , views.CarCreateAPIView.as_view()  ),

    path('Add-Car-photos/' , views.CarPhotoUploadView.as_view()  ),

    path('remove_Car/' , views.remove_Car  ),

    path('Update-Car-Info/', views.CarsInfoUpdateAPIView.as_view(), name='cars-info-update'),

]
