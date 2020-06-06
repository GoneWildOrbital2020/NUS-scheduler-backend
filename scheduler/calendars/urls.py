from django.urls import path
from .views import day_events, all_events

urlpatterns = [
    path('<int:user_id>/<int:month>/<int:day>', day_events),
    path('<int:user_id>', all_events)
]
