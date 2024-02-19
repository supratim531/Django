from .models import *
from rest_framework import serializers

def roll_should_not_exceed_1000(value):
  if value <= 0:
    raise serializers.ValidationError("Roll number can't be 0 or negative")
  elif value > 1000:
    raise serializers.ValidationError("Roll number must be less than or equal 1000")

  return value

class StudentSerializer(serializers.ModelSerializer):
  roll_number = serializers.IntegerField(validators=[roll_should_not_exceed_1000])

  class Meta:
    model = Student
    exclude = ["registration_number"]
