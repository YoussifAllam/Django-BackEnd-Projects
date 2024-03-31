from django.shortcuts import render

# Create your views here.
# serializers.py

# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .serializers import UserSerializer

class UserLoginAPIView(APIView):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request):
        username = request.data.get('Username')
        password = request.data.get('Password')
        if not username or not password:
            return Response({'error': 'Username and Password is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            serializer = UserSerializer(user)
            json = {
                    "status": "success",
                    'data' : serializer.data
            }
            return Response(json, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'There is no user with this info'}, status=status.HTTP_401_UNAUTHORIZED)
