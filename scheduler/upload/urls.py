from django.urls import path
from .views import upload_file, upload_image, upload_note, get_all_files, get_all_images, get_all_notes, delete_notes, delete_files, get_total_notes, get_total_files

urlpatterns = [
    path('file/<str:name>', upload_file),
    path('image/<str:name>', upload_image),
    path('note/<str:name>', upload_note),
    path('get/file/<str:name>', get_all_files),
    path('get/image/<str:name>', get_all_images),
    path('get/note/<str:name>', get_all_notes),
    path('delete/note/<str:name>', delete_notes),
    path('delete/files/<str:name>', delete_files),
    path('get/totalnotes/', get_total_notes),
    path('get/totalfiles/', get_total_files),
]
