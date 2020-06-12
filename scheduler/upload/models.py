from django.db import models

def upload_path(instance, filename):
    return '/'.join([str(instance.name), filename])

class Module(models.Model):
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.code

class FileHolder(models.Model):
    name = models.CharField(max_length=200, unique=True)
    image = models.ImageField(blank=True, null=True, upload_to=upload_path)
    file = models.FileField(blank=True, null=True, upload_to=upload_path)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name