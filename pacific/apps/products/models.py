from django.db import models

# Create your models here.
class Category1(models.Model):
    Title = models.CharField(max_length=30)
    Main_image = models.ImageField(upload_to='main_images/')
    Cover_image = models.ImageField(upload_to='Category1_cover_images/')

    def __str__(self):
        return self.Title
    

class Category2(models.Model):
    Product_Name = models.CharField(max_length=30)
    Product_image = models.ImageField(upload_to='Category2_Products_images/')
    Product_Desc = models.TextField()
    Is_Catogry =  models.BooleanField(default=False)
    Main_category_fk = models.ForeignKey(Category1, on_delete=models.CASCADE, related_name='categoryes')

    def __str__(self):
        return self.Product_Name
    
class Category3(models.Model):
    Product_Name = models.CharField(max_length=30)
    Product_image = models.ImageField(upload_to='Category3_Products_images/')
    Product_Desc = models.TextField()
    category2_fk = models.ForeignKey(Category2, on_delete=models.CASCADE, related_name='categoryes2')

    def __str__(self):
        return self.Product_Name
    
class Category3_coverIamge(models.Model):
    Image = models.ImageField(upload_to='Category3_cover_images/')
    category3_fk = models.ForeignKey(Category2, on_delete=models.DO_NOTHING, related_name='categoryes3')
    
# class Category2_coverPhoto(models.Model):