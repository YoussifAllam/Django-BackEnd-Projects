from django.db import models

class Sponsors_Model(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Sponsors_logos/')
    phone_number =models.CharField(max_length=20)
    work_fields = models.CharField(max_length=100)

    def __str__(self):
        return self.name