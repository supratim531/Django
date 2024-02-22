import uuid
from django.db import models

# Create your models here.
class Student(models.Model):
  reg_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  roll = models.IntegerField()
  name = models.CharField(max_length=255)
  city = models.CharField(max_length=255)
  passby = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True, editable=True)

  def __str__(self):
    return f"{self.name} (roll: {self.roll}) [id: {self.reg_id}]"
