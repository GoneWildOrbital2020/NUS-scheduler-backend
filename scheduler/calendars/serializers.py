from rest_framework import serializers
from events.models import Event


class MonthSerializer(serializers.ModelSerializer):

    day = serializers.StringRelatedField()

    class Meta:
        model = Event
        fields = '__all__'
