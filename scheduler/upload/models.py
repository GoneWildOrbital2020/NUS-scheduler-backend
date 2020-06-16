from django.db import models
from users.models import UserCustom

def upload_path(instance, filename):
    return '/'.join([str(instance.name), filename])

class EventGroup(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(UserCustom, on_delete=models.CASCADE, null=True, blank=True, related_name='owner')

    def __str__(self):
        return self.name

class FileHolder(models.Model):
    name = models.CharField(max_length=200)
    file = models.FileField(blank=True, null=True, upload_to=upload_path)
    group = models.ForeignKey(EventGroup, on_delete=models.CASCADE, null=True, blank=True, related_name='files')

    def __str__(self):
        return self.name

class ImageHolder(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True, upload_to=upload_path)
    group = models.ForeignKey(EventGroup, on_delete=models.CASCADE, null=True, blank=True, related_name='images')

    def __str__(self):
        return self.name