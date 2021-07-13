from django.db.models import Count
from rest_framework import serializers
from .models import Song


class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'album', 'release_date', 'like']