from django.urls import path 
from . import views
app_name = 'accounts'

urlpatterns = [
path('doctors/',views.doctor_list , name= 'doctor_list'),
path('login/',views.login_user , name= 'login'),
path('myprofile/',views.myprofile , name= 'myprofile'),
path('update_profile/',views.update_profile , name= 'update_profile'),
path('signup/',views.signup , name= 'signup'),
path('<slug:doctorslug>/',views.doctor_detail_function , name= 'doctor_detail'),


]
