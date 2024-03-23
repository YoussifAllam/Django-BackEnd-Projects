from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ImageSerializer
from .models import Image
from .tasks import classify_image



class ImageUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        image_serializer = ImageSerializer(data=request.data)
        if image_serializer.is_valid():
            image_serializer.save()
            image = Image.objects.get(id=image_serializer.data['id'])
            # Assume classify_image is a function that takes an image file and returns the class
            classification_result = classify_image(image.picture)
            return Response({'class': classification_result}, status=200)
        else:
            return Response(image_serializer.errors, status=400)
