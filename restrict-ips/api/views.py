from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class TestAPIView(APIView):
  def get(self, request, format=None):
    return Response({
      "message": "Working"
    }, status=status.HTTP_200_OK)
