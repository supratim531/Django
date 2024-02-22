from .models import *
from django.contrib import admin

# Register your models here.
@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
  list_display = [i.name for i in Singer._meta.fields]

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
  list_display = [i.name for i in Song._meta.fields]
