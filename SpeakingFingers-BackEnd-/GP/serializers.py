from rest_framework import serializers

class AudioFileSerializer(serializers.Serializer):
    audio_file = serializers.FileField()
