from django.urls import path
from .views import day_events, all_events, check_leap

urlpatterns = [
    path('<str:username>/<int:year>/<int:month>/<int:day>', day_events),
    path('checkleap/<int:year>', check_leap),
    path('<str:username>/<int:year>', all_events),
]
