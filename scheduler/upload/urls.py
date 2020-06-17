from django.urls import path
from .views import upload_file, upload_image, get_all_files, get_all_images

urlpatterns = [
    path('file/<str:name>', upload_file),
    path('image/<str:name>', upload_image),
    path('get/file/<str:username>/<str:name>', get_all_files),
    path('get/image/<str:username>/<str:name>', get_all_images),
]
