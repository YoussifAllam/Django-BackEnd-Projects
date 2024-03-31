from django.shortcuts import render
from .serializers import FrameSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import Track_numbers
from rest_framework.permissions import IsAuthenticated

class HandTrackingAPI(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        l = Track_numbers()
        
        return Response({ 
                         'Status:':'Success',
                         'sign_language_numbers': l[1:]
                         })
    
# Create your views here.
