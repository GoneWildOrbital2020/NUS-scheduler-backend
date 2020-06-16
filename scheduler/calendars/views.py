import json

from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from .models import Year, Day, Month
from users.models import UserCustom
from events.models import Event
from upload.models import EventGroup
from upload.serializers import FileSerializer, ImageSerializer


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated, ])
def day_events(request, username, month, day):
    if request.method == 'GET':
        user_obj = UserCustom.objects.get(username=username)
        year_obj, _ = user_obj.year_set.get_or_create(index=2020)
        month_obj, _ = year_obj.month_set.get_or_create(
            month_name=Month.get_month_code(month))
        day_obj, _ = month_obj.day_set.get_or_create(index=day)
        serialized_events = serializers.serialize(
            'json', day_obj.event_set.all())
        return HttpResponse(serialized_events, content_type='application/json')
    elif request.method == 'POST':
        body = json.loads(request.body)
        events = body['events']
        user_obj = UserCustom.objects.get(username=username)
        year_obj = user_obj.year_set.get(index=2020)
        month_obj = year_obj.month_set.get(
            month_name=Month.get_month_code(month))
        day_obj = month_obj.day_set.get(index=day)
        day_obj.event_set.all().delete()

        for event in events:
            event['day'] = day_obj
            Event.objects.create(**event)
        return HttpResponse(status=200)


@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def all_events(request, username):
    events_count = Event.objects.filter(
        day__month__year__index=2020, day__month__year__user__username=username).count()
    serialized_events = json.dumps({"count": events_count})

    return HttpResponse(serialized_events, content_type='application/json')

@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
@parser_classes([MultiPartParser, FormParser, ])
def upload_file(request, name):
    group_obj = EventGroup.objects.get(name=name)
    file = FileSerializer(data=request.data)
    if file.is_valid():
        instance = file.save()
        instance.group = group_obj
        instance.save()
        return Response(file.data, status=status.HTTP_201_CREATED)
    else:
        return Response(file.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
@parser_classes([MultiPartParser, FormParser, ])
def upload_image(request, name):
    group_obj = EventGroup.objects.get(name=name)
    img = ImageSerializer(data=request.data)
    if img.is_valid():
        instance = img.save()
        instance.group = group_obj
        instance.save()
        return Response(img.data, status=status.HTTP_201_CREATED)
    else:
        return Response(img.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def get_all_files(request, username, name):
    user_obj = UserCustom.objects.get(username=username)
    group_obj = user_obj.owner.get(name=name)
    serialized_files = serializers.serialize('json', group_obj.files.all())
    return HttpResponse(serialized_files, content_type='application/json')

@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def get_all_images(request, username, name):
    user_obj = UserCustom.objects.get(username=username)
    group_obj = user_obj.owner.get(name=name)
    serialized_files = serializers.serialize('json', group_obj.images.all())
    return HttpResponse(serialized_files, content_type='application/json')