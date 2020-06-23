from django.urls import path
from .views import nusmod

urlpatterns = [path("nusmod/<str:username>", nusmod)]
