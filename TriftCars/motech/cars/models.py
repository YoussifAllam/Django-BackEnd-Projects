from django.db import models
import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.



class Cars_Info(models.Model):
   

    control_type = [    
        ('AUTOMATIC', 'AUTOMATIC'),
        ('Manual', 'Manual'),
        ('steptronic', 'steptronic'),
    ]

    Fuel_Type = [
        ('Petrol', 'Petrol'),
        ('Gas', 'Gas'),
        ('FLEXIBLE FUEL', 'FLEXIBLE FUEL'),
        ('Electric', 'Electric'),
    ]

    Cylinders_type = [
        ('4', '4'),
        ('6', '6'),
        ('8', '8'),
    ]

    Make = models.CharField(max_length= 50 ,blank = True, null = True)
    Car_model_name = models.CharField(max_length= 50,blank = True, null = True  )
    status =  models.CharField(max_length= 20 ,blank = True, null = True ) # new , used 
    price  = models.CharField(max_length= 40 , blank = True, null = True) 
    production_year = models.IntegerField (blank = True, null = True)
    mileage  = models.CharField(max_length = 30,blank = True, null = True) # number of miles that the cat done
    Car_Color = models.CharField(max_length=30,blank = True, null = True)
    engine_capacity = models.CharField(max_length=30,blank = True, null = True)
    Body_styel = models.CharField(max_length=30,blank = True, null = True)
    Drive = models.CharField(max_length=30,blank = True, null = True)
    car_code = models.CharField(max_length = 30,  unique=True ,blank = True, null = True)
    Cylinders_type = models.CharField(choices=Cylinders_type,max_length=20,blank = True, null = True)
    Transmission = models.CharField(choices=control_type,max_length=20,blank = True, null = True ) # e.g., manual, automatic, CVT
    Fuel_Type = models.CharField(choices=Fuel_Type,max_length=20,blank = True, null = True )
    description = models.TextField(blank = True, null = True)
    class Meta:
        verbose_name_plural = "Cars Info"
        ordering = [ '-price']

    def __str__(self):
        return f" {self.Car_model_name} , Car Num : {self.pk} "


class CarPhoto(models.Model):
    car = models.ForeignKey(Cars_Info, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(upload_to='cars_photos/' , default='cars_photos/DefualtCarPhoto.jpg')

    def __str__(self):
        return f"Photo for {self.car.Car_model_name} , Car num : {self.car.pk} ,  Photo num {self.pk}"


class num_of_vistors(models.Model):
    num_of_vistors = models.IntegerField(default=0)
