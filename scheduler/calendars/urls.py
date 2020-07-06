from django.urls import path
from .views import day_events, all_events, month_events

urlpatterns = [
    path('<str:username>/<int:month>/<int:day>', day_events),
    path('<str:username>/<int:month>', month_events),
    path('<str:username>', all_events),
]
