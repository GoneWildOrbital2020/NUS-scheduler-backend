from rest_framework import serializers
from .models import EventGroup, Event, RepeatedEvent


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'
        depth = 3


class RepSerializer(serializers.ModelSerializer):
    events = EventSerializer(read_only=True, source="event_set", many=True)

    class Meta:
        model = RepeatedEvent
        fields = ('name', 'events', 'id')


class EventByGroupSerializer(serializers.ModelSerializer):
    rep = RepSerializer(read_only=True, source="repeated", many=True)

    class Meta:
        model = EventGroup
        fields = ('name', 'rep')
