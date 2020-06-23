from django.shortcuts import render
from django.http import HttpResponse
from users.models import UserCustom
from .models import Event
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


@api_view(['POST'])
@permission_classes([AllowAny])
def nusmod(request, username):
    user = UserCustom.objects.get(username=username)
    ics = request.data['ics']
    events = ics.split("BEGIN:VEVENT\r\n")[1:]
    for event in events:
        Event.parse(event, user)
    return HttpResponse(status=200)
