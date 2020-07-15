from django.urls import path
from .views import nusmod, get_event_group_names, event_group, event_view, repeated_event, group, repeated

urlpatterns = [
    path("rep/<str:name>", repeated),
    path("nusmod/", nusmod),
    path("<str:name>", event_group),
    path("<int:event_id>", event_view),
    path("", get_event_group_names),
    path("<str:name>/<int:rep_id>/all", group),
    path("<str:name>/<int:rep_id>", repeated_event),
]
