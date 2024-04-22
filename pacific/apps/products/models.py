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
    # Is_Catogry =  models.BooleanField(default=False)
    Main_category_fk = models.ForeignKey(Category1, on_delete=models.CASCADE, related_name='categoryes' ,verbose_name='Category 1 Name')
    Cover_image = models.ImageField(upload_to='Category3_cover_images/')

    def __str__(self):
        return self.Product_Name
    
# class Category3(models.Model):
#     Product_Name = models.CharField(max_length=30)
#     Product_image = models.ImageField(upload_to='Category3_Products_images/')
#     category2_fk = models.ForeignKey(Category2, on_delete=models.CASCADE, related_name='categoryes2' , verbose_name='Category 2 Name')

#     def __str__(self):
#         return self.Product_Name


#________________________________________________________________
class Final_Product(models.Model):
    Product_Name = models.CharField(max_length=30)
    Product_image = models.ImageField(upload_to='Category3_Products_images/')
    category2_fk = models.ForeignKey(Category1, on_delete=models.CASCADE, related_name='categories2' , verbose_name='Category 2 Name')

    def __str__(self):
        return self.Product_Name

class Benefits_for_Final_Product(models.Model):
    category3_fk = models.ForeignKey(Final_Product, on_delete=models.CASCADE, related_name='Benefits_for_Category3')
    Benefit = models.CharField(max_length=255)
    
class Weights_for_Final_Product(models.Model):
    category3_fk = models.ForeignKey(Final_Product, on_delete=models.DO_NOTHING, related_name='Weights_for_Category3')
    Weight = models.CharField(max_length=15)
    
class grinding_for_Final_Product(models.Model):
    category3_fk = models.ForeignKey(Final_Product, on_delete=models.DO_NOTHING, related_name='grinding_for_Category3')
    grinding_Type = models.CharField(max_length=50)

#________________________________________________________________

class Final_Product_For_C2(models.Model):
    Product_Name = models.CharField(max_length=30)
    Product_image = models.ImageField(upload_to='Category3_Products_images/')
    category2_fk = models.ForeignKey(Category2, on_delete=models.CASCADE, related_name='categoryes31' , verbose_name='Category 2 Name')

    def __str__(self):
        return self.Product_Name

class Benefits_for_C3(models.Model):
    category3_fk = models.ForeignKey(Final_Product_For_C2, on_delete=models.CASCADE, related_name='Benefits_for_Final_Product_For_C2')
    Benefit = models.CharField(max_length=255)
    
class Weights_for_C3(models.Model):
    category3_fk = models.ForeignKey(Final_Product_For_C2, on_delete=models.DO_NOTHING, related_name='Weights_for_Final_Product_For_C2')
    Weight = models.CharField(max_length=15)
    
class grinding_for_C3(models.Model):
    category3_fk = models.ForeignKey(Final_Product_For_C2, on_delete=models.DO_NOTHING, related_name='grinding_for_Final_Product_For_C2')
    grinding_Type = models.CharField(max_length=50)