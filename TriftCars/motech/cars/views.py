from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from .forms import CarsInfoForm, CarPhotoFormSet  # Assuming you have a CarsInfoForm
# from django.http.response import JsonResponse
from .models import Cars_Info , num_of_vistors
from .serializers import Cars_Serializer , Vistors_serializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator

# from rest_framework.views import APIView
# from rest_framework.authentication import BasicAuthentication , TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
from django.http import  Http404
# from django.shortcuts import get_object_or_404


class Num_of_vistors(viewsets.ModelViewSet):
    queryset = num_of_vistors.objects.all()
    serializer_class = Vistors_serializer

    def list(self, request, *args, **kwargs):
        visitor_counter, created = num_of_vistors.objects.get_or_create(id=1)


        formatted_response = {
            "status": "success",
            "visitor_counter" : visitor_counter.num_of_vistors ,

        }

        return Response(formatted_response)

@api_view(['GET'])  # This decorator specifies that this view accepts only GET requests.
def get_car_by_name(request):
    # Accessing 'car_name' from the query parameters
    car_name = request.GET.get('car_name', None)

    if car_name is None:
        return Response({"detail": "Car name is required as a query parameter."}, status=400)

    try:
        car = Cars_Info.objects.get(Car_model_name__iexact=car_name)
    except Cars_Info.DoesNotExist:
        raise Http404("Car not found")

    # Serializing the car object
    serializer = Cars_Serializer(car, context={'request': request})
    return Response(serializer.data)


def create_car_with_photos(request):
    if request.method == 'POST':
        form = CarsInfoForm(request.POST)
        formset = CarPhotoFormSet(request.POST, request.FILES)
        if form.is_valid() and formset.is_valid():
            car_info = form.save()
            formset.instance = car_info
            formset.save()
            return redirect('some_view_name')
    else:
        form = CarsInfoForm()
        formset = CarPhotoFormSet()
    return render(request, 'your_template.html', {'form': form, 'formset': formset})



@method_decorator(never_cache, name='dispatch')
class viewsets_GetAllCars(viewsets.ModelViewSet):
    queryset = Cars_Info.objects.all()
    serializer_class = Cars_Serializer

    def list(self, request, *args, **kwargs):
        response = super(viewsets_GetAllCars, self).list(request, *args, **kwargs)
        visitor_counter, created = num_of_vistors.objects.get_or_create(id=1)
        visitor_counter.num_of_vistors += 1
        visitor_counter.save()

        formatted_response = {
            "status": "success",
            "visitor_counter" : visitor_counter.num_of_vistors ,
            "data": {
                "Cars": response.data
            }
        }

        return Response(formatted_response)



@api_view(['GET'])
def Filter_cars(request):
    cars = Cars_Info.objects.all()

    model = request.GET.get('Model_of_car')
    price_from = request.GET.get('price_from')
    price_to = request.GET.get('price_to')
    Status_of_car = request.GET.get('Status_of_car')

    Type = request.GET.get('Type') # todo ------------------------

    carion_year = request.GET.get('carion_year')
    Trasmission = request.GET.get('Trasmission')

    # print(cars , '\n================================')
    if model:             cars = cars.filter(Car_model_name__icontains=model)

    if price_from:        cars = cars.filter(price__gte=price_from)

    if price_to:          cars = cars.filter(price__lte=price_to)

    if Status_of_car:     cars = cars.filter(status__icontains=Status_of_car)

    if carion_year:   cars = cars.filter(carion_year__icontains=carion_year)

    if Trasmission:       cars = cars.filter(control_type__icontains=Trasmission)

    serializer = Cars_Serializer(cars, many=True, context={'request': request})
    return Response(serializer.data)

