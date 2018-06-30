from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers


class ListAllImage(APIView):

    def get(self, request, format=None):

        all_images = models.Image.objects.all()

        serializedImages = serializers.ImageSerializer(all_images, many=True)

        return Response(data=serializedImages.data)
