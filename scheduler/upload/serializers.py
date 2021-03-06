from rest_framework import serializers
from .models import FileHolder, EventGroup, ImageHolder, Note

class FileSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = FileHolder
        fields = ['identifier', 'name', 'file']

class ImageSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = ImageHolder
        fields = ['identifier', 'name', 'image']

class NoteSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Note
        fields = ['identifier', 'title', 'text']
