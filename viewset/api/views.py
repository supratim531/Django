from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet

# Create your views here.
class StudentViewSet(ViewSet):
  def list(self, request):
    students = Student.objects.all()
    serializedStudents = StudentSerializer(students, many=True)
    students = serializedStudents.data

    if len(students) != 0:
      return Response({
        "error": False,
        "students": students
      })
    else:
      return Response({
        "error": True,
        "message": "No student found"
      }, status=status.HTTP_404_NOT_FOUND)
  
  def retrieve(self, request, pk):
    student = None
    roll_number = pk

    try:
      student = Student.objects.get(roll_number=roll_number)
    except:
      return Response({
        "error": True,
        "message": f"No student fount with roll number {roll_number}"
      }, status=status.HTTP_404_NOT_FOUND)

    serializedStudent = StudentSerializer(student)
    student = serializedStudent.data

    return Response({
      "error": False,
      "student": student
    })
  
  def partial_update(self, request, pk):
    payload = request.data
    old_student = None
    roll_number = pk

    try:
      old_student = Student.objects.get(roll_number=roll_number)
    except:
      return Response({
        "error": True,
        "message": f"No student fount with roll number {roll_number}"
      }, status=status.HTTP_404_NOT_FOUND)

    deserializedStudent = StudentSerializer(old_student, data=payload, partial=True)

    if deserializedStudent.is_valid():
      serializedStudent = StudentSerializer(deserializedStudent.save())
      student = serializedStudent.data

      return Response({
        "error": False,
        "message": f"Student {old_student.full_name} ({old_student.registration_number}) updated successfully",
        "student": student
      })

class StudentFullViewSet(ModelViewSet):
  lookup_field = "roll_number"
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
