from django.urls import path
from .views import day_events, all_events, upload_file, upload_image, get_all_files, get_all_images

urlpatterns = [
    path('<str:username>/<int:month>/<int:day>', day_events),
    path('<str:username>', all_events),
    path('upload/file/<str:name>', upload_file),
    path('upload/image/<str:name>', upload_image),
    path('get/file/<str:username>/<str:name>', get_all_files),
    path('get/image/<str:username>/<str:name>', get_all_images),
]
