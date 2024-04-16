from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Sponsors_Model
from .serializers import Sponsors_serializer

@api_view(['GET', 'POST'])
def Get_all_Sponsors(request):  
    if request.method == 'GET':
        All_Rates = Sponsors_Model.objects.all()
        serializer = Sponsors_serializer(All_Rates, many=True, context={'request': request})

        json = {
                "status": "success",
                'data' : serializer.data
        }
        return Response(json,
                        
                         status= status.HTTP_200_OK)
        
    
    if request.method == 'POST':
        
        serializer =Sponsors_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    else:
        return Response({'error': 'Method Not Allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

