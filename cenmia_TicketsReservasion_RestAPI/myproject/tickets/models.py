from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.


class Movie(models.Model):
    hall = models.CharField(max_length=10)
    Movie_name = models.CharField(max_length= 60 )
    date = models.DateField(auto_now_add=True)
    
class Guest(models.Model):
    Guest_name = models.CharField(max_length=20)
    Guest_Moible = models.CharField(max_length=15)


    
class reservation(models.Model):
    user = models.ForeignKey(Guest , related_name="reservation" , on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie , related_name="reservation" , on_delete=models.CASCADE)
    
    
class Blog(models.Model):
    post_title = models.CharField(max_length=50)
    Auther = models.ForeignKey(User , on_delete = models.CASCADE)
    body = models.TextField()
    
@receiver(post_save , sender = settings.AUTH_USER_MODEL)
def token_generator(sender , instance   , created , **kwargs ):
    if created : 
        Token.objects.create(user = instance)