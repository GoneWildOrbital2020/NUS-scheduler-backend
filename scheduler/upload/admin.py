from django.contrib import admin
from .models import EventGroup, FileHolder, ImageHolder
# Register your models here.
admin.site.register(EventGroup)
admin.site.register(FileHolder)
admin.site.register(ImageHolder)