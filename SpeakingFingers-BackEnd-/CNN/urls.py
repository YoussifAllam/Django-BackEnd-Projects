from django.urls import path , include
# from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView # , TokenObtainPairView

#app name 
# app_name = 'Users'
# router = DefaultRouter()
# router.register(r'users', UserViewSet,basename='users') 

urlpatterns = [
     path('predict_class', ImageUploadView.as_view(), name='predict_class'),
]