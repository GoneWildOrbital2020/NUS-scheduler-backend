from django.urls import path
from .views import CreateUserAPIView, login, testAuth

urlpatterns = [
    path('create/', CreateUserAPIView.as_view()),
    path('login/', login),
    path('testauth/', testAuth),
]