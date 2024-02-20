from .models import *
from .serializers import *
from rest_framework import status
from .permissions import CustomPermission
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .authentications import CustomAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes

# Create your views here.
class StudentFullViewSet(ModelViewSet):
  lookup_field = "roll"
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

  # locally implemented
  authentication_classes = [JWTAuthentication]
  permission_classes = [IsAuthenticated]

@api_view(["GET", "POST", "PUT", "PATCH", "DELETE"])
@permission_classes([CustomPermission])
@authentication_classes([CustomAuthentication])
def test_api(request):
  if request.method == "GET":
    return Response({
      "message": "This is GET request"
    })
  elif request.method == "POST":
    return Response({
      "message": "This is POST request"
    }, status=status.HTTP_201_CREATED)
  elif request.method == "PUT":
    return Response({
      "message": "This is PUT request"
    }, status=status.HTTP_202_ACCEPTED)
  elif request.method == "PATCH":
    return Response({
      "message": "This is PATCH request"
    }, status=status.HTTP_200_OK)
  elif request.method == "DELETE":
    return Response(status=status.HTTP_204_NO_CONTENT)
