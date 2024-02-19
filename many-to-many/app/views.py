from .models import Tag, Product
from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TagSerializer, ProductSerializer

# Create your views here.
@api_view(["GET", "POST", "PUT", "PATCH", "DELETE"])
def tag_api(request):
  try:
    if request.method == "GET":
      tag_id = request.query_params.get("tag_id", None)

      if tag_id is not None:
        tag = Tag.objects.get(tag_id=tag_id)
        serializedData = TagSerializer(tag)

        return Response(data={
          "error": False,
          "tag": serializedData.data
        })
      else:
        tags = Tag.objects.all()
        serializedData = TagSerializer(tags, many=True)

        return Response(data={
          "error": False,
          "tags": serializedData.data
        })
    elif request.method == "POST":
      payload = request.data
      deserializedData = TagSerializer(data=payload)

      if deserializedData.is_valid():
        deserializedData.save()
        tag = TagSerializer(deserializedData.data).data

        return Response(data={
          "error": False,
          "message": "A new tag created",
          "tag": tag
        }, status=status.HTTP_201_CREATED)
      else:
        return Response(data={
          "error": True,
          "message": deserializedData.errors
        }, status=status.HTTP_400_BAD_REQUEST)
  except Exception as e:
    return Response(data={
      "error": True,
      "message": str(e)
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "POST", "PATCH"])
def product_api(request):
  try:
    if request.method == "GET":
      prod_id = request.query_params.get("prod_id", None)

      if prod_id is not None:
        product = Product.objects.get(prod_id=prod_id)
        serializedData = ProductSerializer(product)

        return Response(data={
          "error": False,
          "product": serializedData.data
        })
      else:
        products = Product.objects.all()
        serializedData = ProductSerializer(products, many=True)

        return Response(data={
          "error": False,
          "products": serializedData.data
        })
    elif request.method == "POST":
      payload = request.data
      deserializedData = ProductSerializer(data=payload)

      if deserializedData.is_valid():
        product = deserializedData.save()

        for tag_name in payload["tags"]:
          tag = Tag.objects.get(tag_name=tag_name)
          product.tags.add(tag)

        serializedData = ProductSerializer(product)

        return Response(data={
          "error": False,
          "message": f"A new product {product.prod_name} created",
          "product": serializedData.data
        }, status=status.HTTP_201_CREATED)
      else:
        return Response(data={
          "error": True,
          "message": deserializedData.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "PATCH":
      payload = request.data
      prod_id = request.query_params.get("prod_id", None)
      old_product = Product.objects.get(prod_id=prod_id)
      old_product_name = old_product.prod_name
      deserializedData = ProductSerializer(old_product, data=payload, partial=True)

      if deserializedData.is_valid():
        tags = payload.get("tags", None)
        product = deserializedData.save()

        if tags is not None:
          product.tags.clear()

          for tag_name in tags:
            tag = Tag.objects.get(tag_name=tag_name)
            product.tags.add(tag)

        serializedData = ProductSerializer(product)

        return Response(data={
          "error": False,
          "message": f"Product {old_product_name} updated successfully",
          "product": serializedData.data
        }, status=status.HTTP_201_CREATED)
      else:
        return Response(data={
          "error": True,
          "message": deserializedData.errors
        }, status=status.HTTP_400_BAD_REQUEST)
  except Exception as e:
    return Response(data={
      "error": True,
      "message": str(e)
    }, status=status.HTTP_400_BAD_REQUEST)
