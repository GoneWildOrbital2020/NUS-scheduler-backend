from django.urls import path
from .views import day_events, all_events, check_leap, get_year, add_year, delete_year

urlpatterns = [
    path('<str:username>/<int:year>/<int:month>/<int:day>', day_events),
    path('deleteyear/<str:username>/<int:year>', delete_year),
    path('addyear/<str:username>/<int:year>', add_year),
    path('checkleap/<int:year>', check_leap),
    path('getyear/<str:username>', get_year),
    path('<str:username>/<int:year>', all_events),
]
