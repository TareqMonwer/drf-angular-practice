from django.db import models


class Task(models.Model):
    task_name = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    has_reminder = models.BooleanField(default=False)
    reminder_timestamp = models.DateTimeField(null=True, blank=True)
