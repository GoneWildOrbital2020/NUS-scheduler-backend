from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from events.models import EventGroup
from users.models import UserCustom
from .models import FileHolder, ImageHolder
from .serializers import FileSerializer, ImageSerializer, NoteSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
@parser_classes([MultiPartParser, FormParser, ])
def upload_file(request, username, name):
    user_obj = UserCustom.objects.get(username=username)
    group_obj = user_obj.event_group.get(name=name)
    file = FileSerializer(data=request.data)
    total = request.data['identifier']
    if file.is_valid():
        instance = file.save()
        instance.group = group_obj
        instance.save()
        user_obj.total_files = total
        user_obj.save()
        return Response(file.data, status=status.HTTP_201_CREATED)
    else:
        return Response(file.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
@parser_classes([MultiPartParser, FormParser, ])
def upload_image(request, username, name):
    user_obj = UserCustom.objects.get(username=username)
    group_obj = user_obj.event_group.get(name=name)
    img = ImageSerializer(data=request.data)
    total = request.data['identifier']
    if img.is_valid():
        instance = img.save()
        instance.group = group_obj
        instance.save()
        user_obj.total_files = total
        user_obj.save()
        return Response(img.data, status=status.HTTP_201_CREATED)
    else:
        return Response(img.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def upload_note(request, username, name):
    user_obj = UserCustom.objects.get(username=username)
    group_obj = user_obj.event_group.get(name=name)
    total = request.data['total'] + 1
    if group_obj.notes.filter(identifier=request.data['identifier']).exists():
        curr_note = group_obj.notes.get(identifier=request.data['identifier'])
        curr_note.title = request.data['title']
        curr_note.text = request.data['text']
        curr_note.save()
        return Response(status=status.HTTP_200_OK)
    else:
        note = NoteSerializer(data=request.data)
        if note.is_valid():
            instance = note.save()
            instance.group = group_obj
            instance.save()
            user_obj.total_notes = total
            user_obj.save()
            return Response(note.data, status=status.HTTP_201_CREATED)
        else:
            return Response(note.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def get_all_files(request, username, name):
    user_obj = UserCustom.objects.get(username=username)
    group_obj = user_obj.event_group.get(name=name)
    serialized_files = serializers.serialize('json', group_obj.files.all())
    return HttpResponse(serialized_files, content_type='application/json')


@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def get_all_images(request, username, name):
    user_obj = UserCustom.objects.get(username=username)
    group_obj = user_obj.event_group.get(name=name)
    serialized_files = serializers.serialize('json', group_obj.images.all())
    return HttpResponse(serialized_files, content_type='application/json')

@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def get_all_notes(request, username, name):
    user_obj = UserCustom.objects.get(username=username)
    group_obj = user_obj.event_group.get(name=name)
    serialized_files = serializers.serialize('json', group_obj.notes.all())
    return HttpResponse(serialized_files, content_type='application/json')

@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def delete_notes(request, username, name):
    user_obj = UserCustom.objects.get(username=username)
    group_obj = user_obj.event_group.get(name=name)
    note = group_obj.notes.get(identifier=request.data['identifier'])
    note.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def delete_files(request, username, name):
    user_obj = UserCustom.objects.get(username=username)
    group_obj = user_obj.event_group.get(name=name)
    if group_obj.files.filter(identifier=request.data['identifier']).exists():
        file = group_obj.files.get(identifier=request.data['identifier'])
        file.delete()
    if group_obj.images.filter(identifier=request.data['identifier']).exists():
        image = group_obj.images.get(identifier=request.data['identifier'])
        image.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def get_total_notes(request, username):
    user_obj = UserCustom.objects.get(username=username)
    response = {}
    response['total'] = user_obj.total_notes
    return Response(response, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def get_total_files(request, username):
    user_obj = UserCustom.objects.get(username=username)
    response = {}
    response['total'] = user_obj.total_files
    return Response(response, status=status.HTTP_200_OK)