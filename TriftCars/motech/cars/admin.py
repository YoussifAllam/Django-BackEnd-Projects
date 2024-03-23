# cars/admin.py
from django.contrib import admin
from .models import Cars_Info, CarPhoto
from .forms import CarPhotoForm  # Make sure this form is defined
from django.contrib.auth.models import Group


admin.site.site_header  = 'Thrift Cars Admin Panel'
admin.site.site_title  = 'Thrift Cars Admin Panel'

class CarPhotoInline(admin.TabularInline):  # Or admin.StackedInline for a different layout
    model = CarPhoto
    form = CarPhotoForm
    extra = 1  # Number of empty forms to display

class CarsInfoAdmin(admin.ModelAdmin):
    inlines = [CarPhotoInline,]
    list_display =  ('car_code' , 'Car_Company_and_model' , 'price',  'status' , 'production_year' )
    list_filter = ('Make' , 'status')
    search_fields = ('Make' , 'Car_model_name')
    def Car_Company_and_model(self,obj):
        return f'{obj.Make} , {obj.Car_model_name}'
    

admin.site.register(Cars_Info, CarsInfoAdmin)
admin.site.unregister(Group)
