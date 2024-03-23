from django.db import models
from django.core.validators import MaxValueValidator , MinValueValidator
# Create your models here.

class RatingModel(models.Model):
    UserName = models.CharField(max_length=20)
    Num_OF_Stars = models.IntegerField(validators = [MinValueValidator(1) , MaxValueValidator(5)] ) # to control min and max values
    Rate_Desc = models.CharField(max_length=255)
    Rate_date = models.DateField()

    class Meta:
        verbose_name_plural = "Rating Info"
        ordering = ['-Rate_date']

    def __str__(self):
        return f" User : {self.UserName} , rate Num {self.pk} "