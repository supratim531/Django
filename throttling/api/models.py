import uuid
from django.db import models

# Create your models here.
class Student(models.Model):
  st_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  st_roll = models.IntegerField(unique=True)
  st_name = models.CharField(max_length=100)
  email = models.EmailField(max_length=255, null=True, blank=True)
  city = models.CharField(max_length=50)

  def __str__(self):
    return f"{self.st_name} (roll: {self.st_roll}) (id: {self.st_id})"

class Employee(models.Model):
  ROLES = (
    ("DEVELOPER", "Developer"),
    ("MANAGER", "Manager"),
  )

  reg_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  emp_id = models.CharField(max_length=100, null=True, unique=True)
  emp_name = models.CharField(max_length=100)
  emp_email = models.EmailField(max_length=255, unique=True)
  address = models.TextField(null=True, blank=True)
  role = models.CharField(max_length=50, choices=ROLES)

  def __str__(self):
    return f"{self.emp_name} (id: {self.emp_id}) (reg_id: {self.reg_id})"
