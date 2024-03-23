from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator , MinValueValidator


class Meal_Info(models.Model):
    Meal_Title = models.CharField(max_length=15)
    Meal_description = models.TextField()
    
    def __str__(self) -> str:
        return self.Meal_Title


class Meals_Rating(models.Model):
    Targer_Meal = models.ForeignKey(Meal_Info , on_delete=models.CASCADE )
    Target_User = models.ForeignKey(User , on_delete=models.CASCADE )
    Rating_stars = models.IntegerField(validators = [MinValueValidator(1) , MaxValueValidator(5)] ) # to control min and max values
    
    def __str__(self) -> str:
        return f"{self.Targer_Meal}" 

    class Meta:
        unique_together = (('Target_User', 'Targer_Meal'))
        index_together  = (('Target_User', 'Targer_Meal'))
