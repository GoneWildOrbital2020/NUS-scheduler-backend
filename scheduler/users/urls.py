from django.urls import path
from .views import CreateUserAPIView, login, changeUserCredentials

urlpatterns = [
    path('create/', CreateUserAPIView.as_view()),
    path('login/', login),
    path('update/', changeUserCredentials),
]