from django.db import models
from datetime import datetime as dt
# Create your models here.
class productTable(models.Model):
    name = models.CharField( max_length=150 , )
    dsecription = models.TextField(  )
    price = models.DecimalField( max_digits=6 , decimal_places=2 )
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    is_active = models.BooleanField(default=True)
    publish_date =models.DateTimeField(verbose_name='publish date', default= dt.now() )
    

    def __str__(self) -> str:
        return self.name