from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from users.models import UserCustom
from .models import Event
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def nusmod(request, username):
    user = UserCustom.objects.get(username=username)
    ics = request.data['ics']
    events = ics.split("BEGIN:VEVENT\r\n")[1:]
    for event in events:
        Event.parse(event, user)
    return HttpResponse(status=200)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def event_group(request, username, name):
    group = UserCustom.objects.get(
        username=username).event_group.get(name=name)
    serialized_events = serializers.serialize(
        'json', group.event_set.all())
    return HttpResponse(serialized_events, content_type='application/json')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_event_group_names(request, username):
    user = UserCustom.objects.get(
        username=username)
    serialized_groups = serializers.serialize(
        'json', user.event_group.all(), fields=('name'))
    return HttpResponse(serialized_groups, content_type='application/json')
