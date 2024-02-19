from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
  ROLE = (
    ('DEVELOPER', 'DEVELOPER'),
    ('MANAGER', 'MANAGER')
  )

  user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
  first_name =models.CharField(max_length=255, null=True, blank=True)
  last_name =models.CharField(max_length=255, null=True, blank=True)
  email = models.EmailField()
  phone = models.CharField(max_length=10, null=True, blank=True)
  role = models.CharField(max_length=50, choices=ROLE, null=True, blank=True)
  address = models.TextField()

  def __str__(self) -> str:
    return f"{self.user} ({self.first_name} {self.last_name})"
