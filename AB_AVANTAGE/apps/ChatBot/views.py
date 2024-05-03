from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import generator
from rest_framework.decorators import api_view

@api_view(['POST'])
def Generate_Text_wiht_Gemini(request):
    if request.method == 'POST':
        Prompt = request.data.get('Prompt')

        inputs_dict = { 'Template' : 'You are Professional' }
        try :
            Generated_text = generator(Prompt, inputs_dict)
            return Response( {
                'status' : 'success',
                'data' : Generated_text
                }, status=status.HTTP_200_OK)
        except :
            return Response( {'error' : 'An Error Has Accuerd'}, status=status.HTTP_400_BAD_REQUEST)
        
    else  :
        return Response( {'error' : 'Request method not Allowed try POST request'}, status=status.HTTP_400_BAD_REQUEST)

