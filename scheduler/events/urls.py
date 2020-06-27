from django.urls import path
from .views import nusmod, get_event_group_names, event_group

urlpatterns = [path("nusmod/<str:username>", nusmod),
               path("<str:username>/<str:name>", event_group),
               path("<str:username>", get_event_group_names)]
