import json

from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse

from .models import Year, Day, Month
from events.models import Event


def day_events(request, user_id, month, day):
    if request.method == 'GET':
        year_obj, _ = Year.objects.get_or_create(pk=1)
        month_obj, _ = year_obj.month_set.get_or_create(
            month_name=Month.get_month_code(month))
        day_obj, _ = month_obj.day_set.get_or_create(index=day)
        serialized_events = serializers.serialize(
            'json', day_obj.event_set.all())
        return HttpResponse(serialized_events, content_type='application/json')
    elif request.method == 'POST':
        body = json.loads(request.body)
        events = body['events']
        year_obj, _ = Year.objects.get_or_create(pk=1)
        month_obj, _ = year_obj.month_set.get_or_create(
            month_name=Month.get_month_code(month))
        day_obj, _ = month_obj.day_set.get_or_create(index=day)

        for event in events:
            event['day'] = day_obj
            Event.objects.update_or_create(
                index=event['index'], defaults=event)
        return HttpResponse(status=200)


def all_events(request, user_id):
    if request.method == 'GET':
        events_count = Event.objects.filter(day__month__year__pk=1).count()
        serialized_events = json.dumps({"count": events_count})

        return HttpResponse(serialized_events, content_type='application/json')
