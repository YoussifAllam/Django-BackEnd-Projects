from django.db import models

# 1. 👇 Add the following line
class Notification(models.Model):
    message = models.CharField(max_length=100)
    
    def __str__(self):
        return self.message