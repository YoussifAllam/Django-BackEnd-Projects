from django.shortcuts import render
from django.http.response import JsonResponse 
from .models import Guest , Movie , reservation , Blog
from .serializers import Guest_Serializer , Movie_Serializer , reservation_Serializer ,BlogSerializer
from rest_framework import status , filters ,generics , mixins , viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication , TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuther_OrReadOnly
# Create your views here.

def test_with_staticDate(request):
    guests = [
         {
        'id': '1',
        'name': 'youssif',
        'mobile' : '0113'
    },
    
    {
        'id': '2',
        'name': 'omar',
        'mobile' : '235'
    }
    ]
    
    return JsonResponse(guests , safe= False)#safe= False mean  that the data is not encrypted

def test_norest_withModel(request):
    data = Guest.objects.all()
    response = {
        'guests': list(data.values('Guest_name' , 'Guest_Moible')),
    }

    return JsonResponse(response )

#! function baed view
#  GET POST
@api_view(['GET', 'POST'])
def FBV_list(request): # function baed view
    # GET 
    
    print(request.data , '________________________________________________________________')
    if request.method == 'GET':
        guests = Guest.objects.all()
        serializer = Guest_Serializer(guests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST
    elif request.method == 'POST':
        serializer = Guest_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handle other HTTP methods
    else:
        return Response({'error': 'Method Not Allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

# GET DELETE PUT
@api_view(['GET' , 'PUT' , 'DELETE'])
def FBV_PK(request , pk): 
    try:
        Target_Guest = Guest.objects.get(pk = pk)    
    except Guest.DoesNotExist : return Response(status = status.HTTP_404_NOT_FOUND)
    
    # GET
    if request.method == 'GET':
        serializer = Guest_Serializer(Target_Guest)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # PUT
    elif request.method == 'PUT':
        serializer = Guest_Serializer(Target_Guest , data=request.data) # in first we should chosee the guest that i will need to update its data which is Target_Guest
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE
    elif request.method == 'DELETE':
        Target_Guest.delete()
        Response(status=status.HTTP_204_NO_CONTENT)
        
    # Handle other HTTP methods
    else:
        return Response({'error': 'Method Not Allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


#! class Based view
# class GET POSST
class CBV_View(APIView):
    def get(self , request):
        all_Guests = Guest.objects.all() 
        serializer = Guest_Serializer(all_Guests , many=True)
        return Response(serializer.data)
    
    def post(self , request):
        serializer = Guest_Serializer(data = request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class GET PUT DElete
class CBV_View_PK(APIView):
    def get_object(self , pk):
        try :
            return Guest.objects.get(pk = pk) 
        except Guest.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        
    def get(self,request , pk):
        target_Guest = self.get_object(pk)
        serializer = Guest_Serializer(target_Guest )
        return Response(serializer.data)
    
    def put(self , request , pk):
        target_Guest = self.get_object(pk)
        serializer = Guest_Serializer(target_Guest , data = request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request , pk):
        target_Guest = self.get_object(pk)
        target_Guest.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

#! mixins   
# mixins list
class Mixins_list( mixins.ListModelMixin , mixins.CreateModelMixin , generics.GenericAPIView  ):
    queryset = Guest.objects.all()
    serializer_class = Guest_Serializer
    
    def get( self , request):
        return self.list(request)
    
    def post( self , request):
        return self.create(request)
    
    
# mixins Pk
class Mixin_PK(mixins.RetrieveModelMixin , mixins.UpdateModelMixin , mixins.DestroyModelMixin , generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = Guest_Serializer
    
    def get( self , request , pk):
        return self.retrieve(request)
    
    def put( self , request , pk):
        return self.update(request)
    
    def delete( self , request , pk):
        return self.destory(request)
    
    
#! generics
# GET Post
class generics_lsit(generics.ListCreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = Guest_Serializer
    authentication_classes = [TokenAuthentication]
    
    
# GeT put delete
class generics_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = Guest_Serializer
    
#! ViewSets
class viewsets_guest(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = Guest_Serializer
    
class viewsets_Movie(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = Movie_Serializer
    filter_backend = [filters.SearchFilter]
    search_fiels = ['hall' , 'Movie_name']
    
class viewsets_reservation(viewsets.ModelViewSet):
    queryset = reservation.objects.all()
    serializer_class = reservation_Serializer
    
@api_view(['GET'])
def Find_movie(request):
    Target_Movie = Movie.objects.filter(
        Movie_name = request.data['Movie_name'],
        hall = request.data['hall'],
    )
    serializer = Movie_Serializer(Target_Movie , many = True)
    return Response(serializer.data)

@api_view(['POST'])
def new_reservation(request):
    
    Target_Movie = Movie.objects.get(
        Movie_name = request.data['Movie_name'],
        hall = request.data['hall'],
    )
    
    guest_object = Guest.objects.get(
        pk = request.data['pk'],
    )
    if not guest_object :
        guest_object = Guest()
        guest_object.Guest_name  = request.data['Guest_name']
        guest_object.Guest_Moible  = request.data['Guest_Moible']
        guest_object.save()
        
    reservation_object = reservation()
    reservation_object.user = guest_object
    reservation_object.movie = Target_Movie
    reservation_object.save()
    
    
    return Response(status = status.HTTP_201_CREATED)


class Blok_Pk(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuther_OrReadOnly]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer









