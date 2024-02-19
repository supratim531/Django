from .models import *
from django.contrib import admin

# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
  list_display = [i.name for i in Tag._meta.fields]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = [i.name for i in Product._meta.fields]
