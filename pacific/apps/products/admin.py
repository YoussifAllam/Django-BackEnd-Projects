from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Category1)
admin.site.register(Category2)



#________________________________________________________________
class WeightInline(admin.TabularInline):
    model = Weights_for_Final_Product
    extra = 1

class GrindingInline(admin.TabularInline):
    model = grinding_for_Final_Product
    extra = 1

class BenefitInline(admin.TabularInline):
    model = Benefits_for_Final_Product
    extra = 1

class FinalProductAdmin(admin.ModelAdmin):
    inlines = [WeightInline, GrindingInline, BenefitInline]

admin.site.register(Final_Product, FinalProductAdmin)

#________________________________________________________________

class WeightInline_C2(admin.TabularInline):
    model = Weights_for_C3
    extra = 1

class GrindingInline_C2(admin.TabularInline):
    model = grinding_for_C3
    extra = 1

class BenefitInline_C2(admin.TabularInline):
    model = Benefits_for_C3
    extra = 1

class FinalProductAdmin_C2(admin.ModelAdmin):
    inlines = [WeightInline_C2, GrindingInline_C2, BenefitInline_C2]

admin.site.register(Final_Product_For_C2 ,FinalProductAdmin_C2 )