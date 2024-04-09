from django.urls import path
from . import views

urlpatterns = [
    
    path('signin',views.signin , name='signin_page'),
    path('signup',views.signup , name='signup_page'),
    path('profile',views.profile , name='profile_page'),
]