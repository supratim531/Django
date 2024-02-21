from .models import Student, Employee
from rest_framework import serializers
from .generators import employee_id_generator

class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    exclude = ["st_id"]

class EmployeeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Employee
    exclude = ["reg_id"]
    extra_kwargs = {
      "emp_id": {"read_only": True}
    }
  
  def create(self, validated_data):
    validated_data["emp_id"] = employee_id_generator()
    employee = Employee.objects.create(**validated_data)
    return employee
