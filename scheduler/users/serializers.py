from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from .models import UserCustom

class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField()
    password = serializers.CharField(write_only=True)

    class Meta(object):
        model = UserCustom
        fields = ('email', 'username', 'date_joined', 'password')