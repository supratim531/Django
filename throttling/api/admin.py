from django.contrib import admin
from .models import Student, Employee

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
  list_display = [i.name for i in Student._meta.fields if i.name != "st_id"]

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
  list_display = [i.name for i in Employee._meta.fields if i.name != "address" and i.name != "reg_id"]
