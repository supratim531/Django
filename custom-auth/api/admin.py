from .models import *
from django.contrib import admin

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
  list_display = [i.name for i in Student._meta.fields if i.name != "address"]
