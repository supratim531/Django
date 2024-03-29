# Generated by Django 4.2.10 on 2024-02-21 10:23

import api.generators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('reg_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('emp_id', models.CharField(default=api.generators.employee_id_generator, max_length=100, unique=True)),
                ('emp_name', models.CharField(max_length=100)),
                ('emp_email', models.EmailField(max_length=255, unique=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('role', models.CharField(choices=[('DEVELOPER', 'Developer'), ('MANAGER', 'Manager')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('st_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('st_roll', models.IntegerField(unique=True)),
                ('st_name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
    ]
