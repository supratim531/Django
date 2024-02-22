from .models import *
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = "__all__"
    read_only_fields = ["reg_id"]
