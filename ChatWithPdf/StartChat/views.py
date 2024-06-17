from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ImageSerializer
from .models import PDF
from .tasks import Pdf_loader

from rest_framework.permissions import IsAuthenticated

def get_current_host(request):
    protocol = request.is_secure() and 'https' or 'http'
    host = request.get_host()
    return "{protocol}://{host}/".format(protocol=protocol, host=host)

class ImageUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        image_serializer = ImageSerializer(data=request.data)
        if image_serializer.is_valid():
            image_serializer.save()
            pdf_instance = PDF.objects.get(id=image_serializer.data['id'])
            question = request.data.get('question')
            pdf_path = pdf_instance.file.path  # Use the file path instead of URL
            
            arabic_letter = Pdf_loader(pdf_path, question)
            response_data = {
                "status": "success",
                "data": arabic_letter
            }
            return Response(response_data, status=200)
        else:
            return Response(image_serializer.errors, status=400)
