import json
from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from users.models import UserCustom
from .models import Task


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def tasks(request, name):
    username = request.user.username
    if request.method == 'GET':
        data = UserCustom.objects.get(
            username=username).event_group.all().get(name=name).task_set.all()
        return HttpResponse(serializers.serialize('json', data), content_type='application/json')
    elif request.method == 'POST':
        body = json.loads(request.body)
        event_group = UserCustom.objects.get(
            username=username).event_group.all().get(name=name)
        task_obj = Task.objects.create(**body['data'], event_group=event_group)
        return JsonResponse({"id": task_obj.id})


@ api_view(['PUT', 'DELETE'])
@ permission_classes([IsAuthenticated])
def task(request, name, id):
    username = request.user.username
    if request.method == 'DELETE':
        Task.objects.get(pk=id).delete()
        return HttpResponse(status=200)
    elif request.method == 'PUT':
        body = json.loads(request.body)
        Task.objects.filter(pk=id).update(**body['data'])
        return HttpResponse(status=200)
