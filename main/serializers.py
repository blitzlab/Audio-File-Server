from rest_framework import serializers
from .models import Song, Podcast, Audiobook

class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        extra_kwargs = {'audio_type': {'required':True}}
        fields = '__all__'

class PodcastSerializer(serializers.ModelSerializer):

    class Meta:
        model = Podcast
        fields = '__all__'

class AudiobookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Audiobook
        fields = '__all__'