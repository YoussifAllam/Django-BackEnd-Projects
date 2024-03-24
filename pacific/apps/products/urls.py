from django.urls import path , include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Main_categoryes', View_get_all_Category1)

urlpatterns = [
    path('',include(router.urls) ),
    path('get_products_in_C2/' , view=get_products_in_category2),
    
    path('get_products_in_C3/' , view=get_products_in_category3),
    
    path('get_category3_coverIamge/' , view=get_category3_coverIamge)
]