from .models import *
from .serializers import *
from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

# Create your views here.
class CreateReadAllStudentAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    try:
      return self.create(request, *args, **kwargs)
    except Exception as e:
      return Response({
        "error": True,
        "message": str(e)
      }, status=status.HTTP_400_BAD_REQUEST)

class ReadUpdateDeleteStudentAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
  lookup_field = "roll_number"
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

  def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)

  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)

  def patch(self, request, *args, **kwargs):
    return self.partial_update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)
