from django.db import models
from calendars.models import Day
from upload.models import Module


class Event(models.Model):
    index = models.IntegerField()
    title = models.CharField(max_length=30)
    description = models.TextField()
    start = models.TextField()
    end = models.TextField()
    location = models.TextField()
    color = models.TextField(default="#FFFFFF")
    day = models.ForeignKey(Day, on_delete=models.CASCADE, default=1)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
