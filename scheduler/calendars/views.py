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
from .serializers import MonthSerializer


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated, ])
def day_events(request, username, year, month, day):
    if request.method == 'GET':
        user_obj = UserCustom.objects.get(username=username)
        year_obj, _ = user_obj.year_set.get_or_create(index=year, is_leap=Year.check_leap(year))
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
        year_obj = user_obj.year_set.get(index=year)
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
def month_events(request, username, year, month):
    if request.method == 'GET':
        user_obj = UserCustom.objects.get(username=username)
        year_obj, _ = user_obj.year_set.get_or_create(index=year, is_leap=Year.check_leap(year))
        month_obj, _ = year_obj.month_set.get_or_create(
            month_name=Month.get_month_code(month))
        serializer = MonthSerializer(
            Event.objects.filter(day__month=month_obj), many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def all_events(request, username, year):
    events_count = Event.objects.filter(
        day__month__year__index=year, day__month__year__user__username=username).count()
    serialized_events = json.dumps({"count": events_count})

    return HttpResponse(serialized_events, content_type='application/json')

@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def check_leap(request, year):
    response = {}
    response['leap'] = Year.check_leap(year)
    return Response(response, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def get_year(request, username):
    user_obj = UserCustom.objects.get(username=username)
    serialized_years = serializers.serialize('json', user_obj.year_set.all())
    return HttpResponse(serialized_years, content_type='application/json')

@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def add_year(request, username, year):
    user_obj = UserCustom.objects.get(username=username)
    year = Year(index=year, user=user_obj, is_leap=Year.check_leap(year))
    year.save()
    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def delete_year(request, username, year):
    user_obj = UserCustom.objects.get(username=username)
    year = user_obj.year_set.get(index=year)
    year.delete()
    return Response(status=status.HTTP_200_OK)
