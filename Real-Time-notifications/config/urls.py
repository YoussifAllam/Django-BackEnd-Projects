from django.contrib import admin
from django.urls import path, include # 👈 1. Add this line

urlpatterns = [
    path('admin/', admin.site.urls),
    # 👇 2. Add the app url on this
    path('', include('myapp.urls'))
]