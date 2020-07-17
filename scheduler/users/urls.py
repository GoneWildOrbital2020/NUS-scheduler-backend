from django.urls import path
from .views import CreateUserAPIView, login, changeUserCredentials, activate_account, request_remember, reset_password

urlpatterns = [
    path('create/', CreateUserAPIView.as_view()),
    path('login/', login),
    path('update/', changeUserCredentials),
    path('activate/', activate_account),
    path('remember/', request_remember),
    path('reset/', reset_password),
]