from .models import Employee
from django.contrib import admin

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
  list_display = [i.name for i in Employee._meta.fields if i.name != "address"]
