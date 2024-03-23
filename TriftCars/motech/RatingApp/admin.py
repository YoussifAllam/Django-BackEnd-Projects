from django.contrib import admin
from .models import RatingModel
# Register your models here.



admin.site.register(RatingModel )


# class Rating_admin(admin.ModelAdmin):
#     list_display = ['id', 'Targer_Meal' , 'Target_User' , 'Rating_stars']
#     list_filter = [ 'Targer_Meal' , 'Target_User']
        
# class Meal_admin(admin.ModelAdmin):
#     list_display = [ 'id' , 'Meal_Title' , 'Meal_description']
#     search_fields = ['Meal_Title' , 'Meal_description']
#     list_filter = ['Meal_Title' , 'Meal_description']
    
# admin.site.register( Meal_Info , Meal_admin )
# admin.site.register( Meals_Rating , Rating_admin )