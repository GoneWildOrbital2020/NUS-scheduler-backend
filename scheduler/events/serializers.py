from rest_framework import serializers
from .models import EventGroup, Event, RepeatedEvent


class EventSerializer(serializers.ModelSerializer):
    day = serializers.IntegerField(read_only=True, source="day.index")
    month = serializers.CharField(
        read_only=True, source="day.month.month_name")
    year = serializers.IntegerField(
        read_only=True, source="day.month.year.index")

    class Meta:
        model = Event
        fields = ('index', 'title', 'description',
                  'start', 'end', 'location', 'color', 'day', 'month', 'year', 'id')
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
