from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class HandTrackingAPI(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        
        
        return Response({ 
                         'Status:':'Success',
                         'sign_language_numbers': 1
                         })
    
# Create your views here.
