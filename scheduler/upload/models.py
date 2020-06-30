from django.db import models
from django.utils import timezone
from events.models import EventGroup


def upload_path(instance, filename):
    return '/'.join([str(instance.name), filename])


class FileHolder(models.Model):
    name = models.CharField(max_length=200)
    file = models.FileField(blank=True, null=True, upload_to=upload_path)
    group = models.ForeignKey(
        EventGroup, on_delete=models.CASCADE, null=True, blank=True, related_name='files')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ImageHolder(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True, upload_to=upload_path)
    group = models.ForeignKey(
        EventGroup, on_delete=models.CASCADE, null=True, blank=True, related_name='images')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Note(models.Model):
    identifier = models.IntegerField(null=True)
    title = models.CharField(max_length=200, blank=True, null=True, unique=False)
    text = models.TextField(blank=True, null=True, unique=False)
    group = models.ForeignKey(
        EventGroup, on_delete=models.CASCADE, null=True, blank=True, related_name="notes")

    class Meta:
        unique_together = ['identifier', 'group']

    def __str__(self):
        return self.title