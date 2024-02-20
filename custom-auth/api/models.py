import uuid
from django.db import models

# Create your models here.
class Student(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  roll = models.IntegerField(unique=True)
  name = models.CharField(max_length=255)
  address = models.TextField(null=True, blank=True)
