from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import StartUp_Model
from .serializers import StartappsSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def GET_ALL_Startups(request):
        startups = StartUp_Model.objects.all()
        serializer = StartappsSerializer(startups, many=True)
        return Response({
               'status' : 'success',
                'data' : serializer.data} , status=status.HTTP_200_OK)



@api_view(['POST'])
def Add_new_startup(request):
    data = request.data.copy()  # Work with a mutable copy of the request data
    
    # Convert country name to country ID if 'country_name' is provided
    if 'country_name' in data:
        country_dict = {name: id for id, name in StartUp_Model.countries_ids}
        country_id = country_dict.get(data['country_name'])
        
        if country_id is None:
            return Response({
                'status': 'error',
                'message': 'Invalid country name'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        data['country_id'] = country_id  # Replace or set the country_id in data
    
    # Remove country_name to prevent unexpected field error
    data.pop('country_name', None)

    # Proceed with serialization
    serializer = StartappsSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'status': 'success',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
