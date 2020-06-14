from rest_framework import serializers
from .models import FileHolder, EventGroup, ImageHolder

class FileSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = FileHolder
        fields = ['name', 'file']

class ImageSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = ImageHolder
        fields = ['name', 'image']
