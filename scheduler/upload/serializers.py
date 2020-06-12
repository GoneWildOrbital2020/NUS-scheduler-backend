from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from .models import FileHolder, Module

class FileSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = FileHolder
        fields = ['name', 'image', 'file']
