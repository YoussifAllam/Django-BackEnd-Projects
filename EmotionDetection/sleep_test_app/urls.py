from django.urls import path , include
from .views import *
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('sleep_tests/' , include('sleep_test_app.urls'))
    path('check/' , ImageUploadView.as_view())
]
