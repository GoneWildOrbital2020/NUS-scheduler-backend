from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import UserCustom
from scheduler.settings import SECRET_KEY
import jwt
from rest_framework_jwt.utils import jwt_payload_handler

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser, ])
def changeUserCredentials(request):
    email = request.data['email']
    username = request.data['username']
    password = request.data['password']
    avatar = request.data['avatar']
    print(avatar)
    print(username)
    print(email)
    print(password)
    user = UserCustom.objects.get(email=email)
    if avatar != '':
        user.avatar = avatar
        print('here')
    if password != '':
        user.password = password
    user.username = username
    user.save()
    return Response(status=status.HTTP_200_OK) 


@api_view(['POST'])
@permission_classes([AllowAny,])
def login(request):
    try:
        email = request.data['email']
        password = request.data['password']
        user = UserCustom.objects.get(email=email, password=password)
        if user:
            try:
                payload = jwt_payload_handler(user)
                token = jwt.encode(payload, SECRET_KEY)
                user_details = {}
                user_details['email'] = email
                user_details['username'] = user.username
                user_details['token'] = token
                user_details['avatar'] = user.avatar.url
                return Response(user_details, status=status.HTTP_201_CREATED)
            
            except Exception as e:
                raise e
        else:
            res = {
                'error': 'cannot authenticate with the given credentials'
            }
            return Response(res, status=status.HTTP_403_FORBIDDEN)
    
    except KeyError:
        res = {'error': 'please provide an email and a password'}
        return Response(res)


class CreateUserAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)