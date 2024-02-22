import uuid
from django.db import models

# Create your models here.
class Singer(models.Model):
  GENDER = (
    ('M', "Male"),
    ('F', "Female"),
    ('O', "Others")
  )

  singer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  singer_name = models.CharField(max_length=255)
  gender = models.CharField(max_length=2, choices=GENDER)

  def __str__(self):
    return f"{self.singer_name} ({self.singer_id})"

class Song(models.Model):
  song_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  title = models.CharField(max_length=255)
  duration_in_seconds = models.BigIntegerField()
  singer = models.ForeignKey(Singer, null=True, on_delete=models.SET_NULL, related_name="song")

  def __str__(self):
    return f"{self.title} (artist: {self.singer})"
