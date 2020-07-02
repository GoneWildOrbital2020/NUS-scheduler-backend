from django.urls import path
from .views import upload_file, upload_image, upload_note, get_all_files, get_all_images, get_all_notes, delete_notes, delete_files, get_total_notes

urlpatterns = [
    path('file/<str:username>/<str:name>', upload_file),
    path('image/<str:username>/<str:name>', upload_image),
    path('note/<str:username>/<str:name>', upload_note),
    path('get/file/<str:username>/<str:name>', get_all_files),
    path('get/image/<str:username>/<str:name>', get_all_images),
    path('get/note/<str:username>/<str:name>', get_all_notes),
    path('delete/note/<str:username>/<str:name>', delete_notes),
    path('delete/files/<str:username>/<str:name>', delete_files),
    path('get/totalnotes/<str:username>', get_total_notes),
]
