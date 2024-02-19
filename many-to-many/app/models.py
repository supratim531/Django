import uuid
from django.db import models

# Create your models here.
class Tag(models.Model):
  TAGS = (
    ("SUMMER", "SUMMER"),
    ("WINTER", "WINTER"),
    ("SPORTS", "SPORTS"),
  )

  tag_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  tag_name = models.CharField(max_length=100, unique=True, choices=TAGS)
  creation_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.tag_name}"

class Product(models.Model):
  CATEGORIES = (
    ("INDOOR", "INDOOR"),
    ("OUTDOOR", "OUTDOOR"),
  )

  prod_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  prod_name = models.CharField(max_length=255)
  category = models.CharField(max_length=50, null=True, blank=True, choices=CATEGORIES)
  creation_date = models.DateTimeField(auto_now_add=True)
  tags = models.ManyToManyField(Tag)
  
  def __str__(self):
    return f"{self.prod_name} ({self.prod_id})"
