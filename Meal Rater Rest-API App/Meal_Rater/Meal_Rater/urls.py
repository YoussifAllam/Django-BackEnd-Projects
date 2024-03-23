from django.contrib import admin
from django.urls import path , include
from rest_framework import routers
# from django.conf.urls import include
from rest_framework.authentication import BasicAuthentication , TokenAuthentication 

from rest_framework.permissions import IsAuthenticated 

from rest_framework.authtoken.views import obtain_auth_token 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('MealRaterApp/' , include('MealRaterApp.urls'))
    
    
]
