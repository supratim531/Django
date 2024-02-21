from rest_framework import status
from .models import Student, Employee
from rest_framework.views import APIView
from rest_framework.response import Response
from .throttles import EmployeeUserRateThrottle
from .authentications import CustomAuthentication
from .exceptions import NotExistException, ValidationException
from .serializers import StudentSerializer, EmployeeSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import ScopedRateThrottle, AnonRateThrottle
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.
class ListCreateBulkDeleteStudentAPIView(APIView):
  throttle_classes = [ScopedRateThrottle]
  throttle_scope = "student"

  def get(self, request, roll=None):
    serializedStudents = StudentSerializer(Student.objects.all(), many=True)
    students = serializedStudents.data

    if len(students) == 0:
      raise NotExistException(detail="No student found")

    return Response({
      "error": False,
      "students": students
      }, status=status.HTTP_200_OK)

  def post(self, request, roll=None):
    return Response({
      "error": False,
      "message": "Not implemented yet"
    }, status=status.HTTP_200_OK)

  def delete(self, request, roll=None):
    serializedStudents = StudentSerializer(Student.objects.all(), many=True)
    students = serializedStudents.data

    if len(students) == 0:
      raise NotExistException(detail="No student found to delete")

    Student.objects.all().delete()

    return Response({
      "error": False,
      "message": f"All students are deleted"
    }, status=status.HTTP_200_OK)

class RetrieveUpdateDeleteStudentAPIView(APIView):
  throttle_classes = [ScopedRateThrottle]
  throttle_scope = "student"

  def get(self, request, roll):
    if not Student.objects.filter(st_roll=roll).exists():
      raise NotExistException(detail=f"Student doesn't exist of roll {roll}")

    serializedStudent = StudentSerializer(Student.objects.get(st_roll=roll))
    student = serializedStudent.data

    return Response({
      "error": False,
      "student": student
    }, status=status.HTTP_200_OK)

  def put(self, request, roll):
    if not Student.objects.filter(st_roll=roll).exists():
      raise NotExistException(detail=f"Student doesn't exist of roll {roll}")

    payload = request.data
    old_student = Student.objects.get(st_roll=roll)
    deserializedStudent = StudentSerializer(old_student, data=payload)

    if deserializedStudent.is_valid():
      student = StudentSerializer(deserializedStudent.save()).data

      return Response({
        "error": False,
        "message": f"Student of roll {roll} updated successfully",
        "student": student
      }, status=status.HTTP_201_CREATED)
    else:
      raise ValidationException(detail=deserializedStudent.errors, is_str=False)

  def patch(self, request, roll):
    if not Student.objects.filter(st_roll=roll).exists():
      raise NotExistException(detail=f"Student doesn't exist of roll {roll}")

    payload = request.data
    old_student = Student.objects.get(st_roll=roll)
    deserializedStudent = StudentSerializer(old_student, data=payload, partial=True)

    if deserializedStudent.is_valid():
      student = StudentSerializer(deserializedStudent.save()).data

      return Response({
        "error": False,
        "message": f"Student of roll {roll} updated successfully",
        "student": student
      }, status=status.HTTP_201_CREATED)
    else:
      raise ValidationException(detail=deserializedStudent.errors, is_str=False)

  def delete(self, request, roll):
    if not Student.objects.filter(st_roll=roll).exists():
      raise NotExistException(detail=f"Student doesn't exist of roll {roll}")
    
    Student.objects.get(st_roll=roll).delete()

    return Response({
      "error": False,
      "message": f"Student of roll {roll} is deleted"
    }, status=status.HTTP_200_OK)

class ListCreateEmployeeAPIView(ListCreateAPIView):
  queryset = Employee.objects.all()
  serializer_class = EmployeeSerializer
  authentication_classes = [CustomAuthentication]
  permission_classes = [IsAuthenticatedOrReadOnly]
  throttle_classes = [AnonRateThrottle, EmployeeUserRateThrottle]

class RetrieveUpdateDeleteEmployeeAPIView(RetrieveUpdateDestroyAPIView):
  lookup_field = "emp_id"
  queryset = Employee.objects.all()
  serializer_class = EmployeeSerializer
  authentication_classes = [CustomAuthentication]
  permission_classes = [IsAuthenticatedOrReadOnly]
  throttle_classes = [AnonRateThrottle, EmployeeUserRateThrottle]
