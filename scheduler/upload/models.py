from django.db import models

def upload_path(instance, filename):
    return '/'.join([str(instance.name), filename])

class EventGroup(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class FileHolder(models.Model):
    name = models.CharField(max_length=200, unique=True)
    file = models.FileField(blank=True, null=True, upload_to=upload_path)
    group = models.ForeignKey(EventGroup, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class ImageHolder(models.Model):
    name = models.CharField(max_length=200, unique=True)
    image = models.ImageField(blank=True, null=True, upload_to=upload_path)
    group = models.ForeignKey(EventGroup, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name