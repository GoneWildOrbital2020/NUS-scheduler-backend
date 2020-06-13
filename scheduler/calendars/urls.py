from django.urls import path
from .views import day_events, all_events, upload_file, upload_image

urlpatterns = [
    path('<str:username>/<int:month>/<int:day>', day_events),
    path('<str:username>', all_events),
    path('upload/file/<str:name>', upload_file),
    path('upload/image/<str:name>', upload_image),
]
