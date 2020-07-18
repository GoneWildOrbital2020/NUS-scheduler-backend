from django.urls import path
from .views import day_events, all_events, check_leap, get_year, add_year, delete_year, month_events

urlpatterns = [
    path('<int:year>/<int:month>/<int:day>', day_events),
    path('<int:year>/<int:month>', month_events),
    path('deleteyear/<int:year>', delete_year),
    path('addyear/<int:year>', add_year),
    path('checkleap/<int:year>', check_leap),
    path('getyear/', get_year),
    path('<int:year>', all_events),
]
