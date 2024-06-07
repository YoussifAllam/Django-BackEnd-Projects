from django.shortcuts import render

# Create your views here.

def send_emils(request):
    return render( request, 'campaign.html' , {}) #campaign. html