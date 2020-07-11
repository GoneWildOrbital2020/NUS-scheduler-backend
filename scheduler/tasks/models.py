from django.db import models
from events.models import EventGroup


class Task(models.Model):
    COLUMN_CHOICES = (
        ('todo', 'To Do'),
        ('onhold', 'On Hold'),
        ('inprogress', 'In Progress'),
        ('done', 'Done')
    )
    title = models.TextField()
    description = models.TextField()
    due_date = models.DateTimeField(null=True, blank=True)
    column_id = models.CharField(max_length=10, choices=COLUMN_CHOICES)
    index = models.IntegerField()
    event_group = models.ForeignKey(
        EventGroup, on_delete=models.CASCADE, null=True, blank=True)
