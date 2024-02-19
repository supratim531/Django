import uuid
from django.db import models

# Create your models here.
class Student(models.Model):
  registration_number = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  roll_number = models.IntegerField(unique=True)
  full_name = models.CharField(max_length=255)
  email = models.EmailField(max_length=255, null=True, blank=True, unique=True)
  phone = models.CharField(max_length=10, unique=True)
  address = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.full_name} ({self.roll_number})"
