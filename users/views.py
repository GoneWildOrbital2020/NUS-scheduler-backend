from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
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
    user = UserCustom.objects.get(email=email)
    if avatar != '':
        user.avatar = avatar
    if password != '':
        user.password = password
    user.username = username
    user.save()
    response = {}
    response['username'] = username
    response['avatar'] = user.avatar.url
    return Response(response, status=status.HTTP_200_OK) 


@api_view(['POST'])
@permission_classes([AllowAny,])
def login(request):
    try:
        email = request.data['email']
        password = request.data['password']
        user = UserCustom.objects.get(email=email, password=password)
        if user:
            try:
                if user.authenticated:
                    payload = jwt_payload_handler(user)
                    token = jwt.encode(payload, SECRET_KEY)
                    user.logout_time = UserCustom.set_expired()
                    user.save()
                    user_details = {}
                    user_details['email'] = email
                    user_details['username'] = user.username
                    user_details['token'] = token
                    user_details['logout_time'] = user.logout_time
                    if user.avatar == '':
                        user_details['avatar'] = ''
                    else:
                        user_details['avatar'] = user.avatar.url
                    return Response(user_details, status=status.HTTP_201_CREATED)
                else:
                    res = {'error': 'Account is not activated!'}
                    return Response(res, status=status.HTTP_403_FORBIDDEN)
            
            except Exception as e:
                raise e
        else:
            res = {
                'error': 'Login failed, please try again!'
            }
            return Response(res, status=status.HTTP_403_FORBIDDEN)
    
    except KeyError:
        res = {'error': 'Email and password are not provided!'}
        return Response(res)


class CreateUserAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        user = request.data
        email = request.data['email']
        subject = 'Activate Your NUS Scheduler Account'
        message = 'Please click the link below to activate your account.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        serializer = UserSerializer(data=user)
        if serializer.is_valid():
            instance = serializer.save()
            payload = jwt_payload_handler(instance)
            token = jwt.encode(payload, SECRET_KEY)
            link = 'http://localhost:3000/activate/' + email + '/' + token.decode('utf8')
            message = message + '\r\n' + link
            send_mail(subject, message, email_from, recipient_list, fail_silently=False)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def activate_account(request):
    email = request.data['email']
    user_obj = UserCustom.objects.get(email=email)
    user_obj.authenticated = True
    user_obj.save()
    payload = jwt_payload_handler(user_obj)
    token = jwt.encode(payload, SECRET_KEY)
    user_obj.logout_time = UserCustom.set_expired()
    user_obj.save()
    user_details = {}
    user_details['email'] = email
    user_details['username'] = user_obj.username
    user_details['token'] = token
    user_details['logout_time'] = user_obj.logout_time
    if user_obj.avatar == '':
        user_details['avatar'] = ''
    else:
        user_details['avatar'] = user_obj.avatar.url
    return Response(user_details, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([AllowAny, ])
def request_remember(request):
    email = request.data['email']
    user_obj = UserCustom.objects.get(email=email)
    payload = jwt_payload_handler(user_obj)
    token = jwt.encode(payload, SECRET_KEY)
    subject = 'Reset Your NUS Scheduler Account Password'
    message = 'Please click the link below to reset your password.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email, ]
    link = 'http://localhost:3000/reset/' + email + '/' + token.decode('utf8')
    message = message + '\r\n' + link
    send_mail(subject, message, email_from, recipient_list, fail_silently=False)
    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def reset_password(request):
    email = request.data['email']
    password = request.data['password']
    user_obj = UserCustom.objects.get(email=email)
    user_obj.password = password
    user_obj.save()
    return Response(status=status.HTTP_200_OK)