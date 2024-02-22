from .models import *
from rest_framework import serializers

class SingerSerializer(serializers.HyperlinkedModelSerializer):
  # song = serializers.StringRelatedField(many=True, read_only=True)
  song = serializers.SlugRelatedField(many=True, read_only=True, slug_field="title")
  # song = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="song-detail")

  class Meta:
    model = Singer
    fields = "__all__"
    # depth = 1 # it is not working over here for this case
    # temp_fields = [i.name for i in Singer._meta.fields]
    # temp_fields.append("song")
    # fields = temp_fields

class SongSerializer(serializers.HyperlinkedModelSerializer):
  # singer = SingerSerializer()

  class Meta:
    model = Song
    fields = "__all__"
    depth = 1
