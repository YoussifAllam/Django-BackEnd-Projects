from django.shortcuts import render



def products(request):
    return render(request , 'products/products.html',{})

def product(request):
    return render(request , 'products/product.html',{})

def search(request):
    return render(request , 'products/search.html',{})

# Create your views here.
