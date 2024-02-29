from django.contrib import admin
from .models import Guest , Movie , reservation , Blog

# Register your models here.

admin.site.register(Movie)
admin.site.register(Guest)
admin.site.register(reservation)
admin.site.register(Blog)
