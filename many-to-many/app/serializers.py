from .models import *
from rest_framework import serializers

class TagSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tag
    exclude = ["tag_id"]

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    exclude = ["prod_id"]
    depth = 1
