import json

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers
from users.models import UserCustom
from calendars.models import Month, Year
from .models import Event, RepeatedEvent, EventGroup
from .serializers import EventByGroupSerializer, EventSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.forms.models import model_to_dict


@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def nusmod(request):
    username = request.user.username
    user = UserCustom.objects.get(username=username)
    ics = request.data['ics']
    events = ics.split("BEGIN:VEVENT\r\n")[1:]
    for event in events:
        Event.parse(event, user)
    return HttpResponse(status=200)


@api_view(['GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def event_group(request, name):
    username = request.user.username
    if request.method == 'GET':
        group = UserCustom.objects.get(
            username=username).event_group.get(name=name)
        serializer = EventByGroupSerializer(group)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        UserCustom.objects.get(
            username=username).event_group.get(name=name).delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def repeated_event(request, name, rep_id):
    username = request.user.username
    if request.method == 'PUT':
        body = json.loads(request.body)
        UserCustom.objects.get(
            username=username).event_group.get(
                name=name).repeated.all().get(pk=rep_id).event_set.all().update(**body['data'])
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        UserCustom.objects.get(
            username=username).event_group.get(
                name=name).repeated.all().get(pk=rep_id).event_set.all().delete()
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'POST':
        body = json.loads(request.body)
        group = UserCustom.objects.get(
            username=username).event_group.get(name=name)
        rep = UserCustom.objects.get(
            username=username).event_group.get(
                name=name).repeated.all().get(pk=rep_id)
        year_obj, _ = UserCustom.objects.get(
            username=username).year_set.get_or_create(
                index=body['year'], is_leap=Year.check_leap(body['year']))
        month_obj, _ = year_obj.month_set.get_or_create(
            month_name=Month.get_month_code(body['month']))
        day_obj, _ = month_obj.day_set.get_or_create(index=body['day'])
        obj = Event.objects.create(
            **body['data'], group=group, repeated_event=rep, day=day_obj)
        serializer = EventSerializer(obj)
        return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def group(request, name, rep_id):
    username = request.user.username
    if request.method == 'DELETE':
        UserCustom.objects.get(
            username=username).event_group.get(
                name=name).repeated.all().get(pk=rep_id).delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def get_event_group_names(request):
    username = request.user.username
    if request.method == 'GET':
        user = UserCustom.objects.get(username=username)
        serialized_groups = serializers.serialize(
            'json', user.event_group.all(), fields=('name'))
        return HttpResponse(serialized_groups, content_type='application/json')
    elif request.method == 'POST':
        body = json.loads(request.body)
        user = UserCustom.objects.get(username=username)
        EventGroup.objects.create(user=user, name=body['name'])
        return Response(status=status.HTTP_200_OK)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def event_view(request, event_id):
    if request.method == 'PUT':
        body = json.loads(request.body)
        Event.objects.filter(pk=event_id).update(**body['data'])
    elif request.method == 'DELETE':
        Event.objects.filter(pk=event_id).delete()
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def repeated(request, name):
    username = request.user.username
    if request.method == 'POST':
        body = json.loads(request.body)
        group = UserCustom.objects.get(
            username=username).event_group.get(name=name)
        rep = RepeatedEvent.objects.create(name=body['name'], group=group)
        return HttpResponse(json.dumps({"id": rep.id}), content_type='application/json')
