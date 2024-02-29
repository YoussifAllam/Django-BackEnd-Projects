
from django.contrib import admin
from django.urls import path , include
from tickets import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
router = DefaultRouter()
router.register('guest', views.viewsets_guest)
router.register('movie', views.viewsets_Movie)
router.register('reservations', views.viewsets_reservation)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('django/jsonresponenomodel', views.test_with_staticDate),
    
    path('django/json_respone_norest_model', views.test_norest_withModel),
    
    #! GET POST from rest
    path('rest/FBV/', views.FBV_list),
    
    #! GET DELETE PUT
    path('rest/FBV_PK/<int:pk>', views.FBV_PK),

    
    #! Class Based View
    path('rest/CBV', views.CBV_View.as_view()),
    
    path('rest/CBV_PK/<int:pk>', views.CBV_View_PK.as_view()),
    
    #! mixins 
    path('rest/mixins_list', views.Mixins_list.as_view()),
    path('rest/mixins_PK/<int:pk>', views.Mixin_PK.as_view()),
    
    #! generics
    path('rest/generic_list', views.generics_lsit.as_view()),
    path('rest/generic_PK/<int:pk>', views.generics_pk.as_view()),
    
    #! veiwsets
    path('rest/viewsets/', include(router.urls)),
    
    
    
    path('FBV/Find_movie/', views.Find_movie),
    
    path('FBV/Create_reservation/', views.new_reservation),
    
    path('api-auth-token' , obtain_auth_token  ) , 
    
    
    path('Blog/generics/' , views.Blok_Pk.as_view()  ) , 
    path('Blog/generics_pk/<int:pk>' , views.Blok_Pk.as_view()  ) , 
]
