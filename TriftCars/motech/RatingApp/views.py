from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import RatingModel
from .serializers import Rating_serializer

from rest_framework.authentication import   TokenAuthentication
from rest_framework.permissions import AllowAny , IsAuthenticated , IsAdminUser , IsAuthenticatedOrReadOnly

# Create your views here.
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def Rating_FBV(request): # function baed view
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]  
    if request.method == 'GET':
        All_Rates = RatingModel.objects.all()
        serializer = Rating_serializer(All_Rates, many=True, context={'request': request})
        return Response(serializer.data , status= status.HTTP_200_OK)
        
    
    if request.method == 'POST':
        
        serializer =Rating_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    else:
        return Response({'error': 'Method Not Allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

