from .models import Employee
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save

@receiver(post_save, sender=User)
def create_or_update_employee_from_user(sender, instance, created, **kwargs):
  if created:
    Employee.objects.create(user=instance, first_name="Sayan", last_name="Das", email=instance.email, phone="6291462153", role="DEVELOPER")
    print(f"CREATED: {instance}, {type(instance)} ({created})")
    pass
  else:
    employee = Employee.objects.get(user=instance)
    print(f"employee: {employee}")
    employee.first_name = instance.first_name
    employee.last_name = instance.last_name
    employee.email = instance.email
    employee.save()
    print(f"UPDATED: {instance}, {type(instance)} ({created})")
    pass
