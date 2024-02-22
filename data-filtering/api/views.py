from .models import *
from .serializers import *
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.authentication import SessionAuthentication

# Create your views here.
class StudentListAPIView(ListAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  # authentication_classes = [SessionAuthentication]
  filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
  filterset_fields = ["city"] # -> this is for DjangoFilterBackend
  search_fields = ["^name"]
  # ordering_fields = ["city"] # if not mentioned then it will use all fields by default
  # search_fields = ["name", "city", "passby"]
  # search_fields = ["^name", "city"] # it implies startswith character for name fields and this is for SearchFilter

  def get_queryset(self):
    username = self.request.user
    print(f"USER: {username}")

    if username.username == "root":
      return Student.objects.all()
    else:
      return Student.objects.filter(passby=username)
