
from django.urls import path 
from .  views  import ImageUploadView
urlpatterns = [
    path('PDF_Loader/' ,  ImageUploadView.as_view()),
]
