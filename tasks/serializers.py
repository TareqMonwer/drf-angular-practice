from dataclasses import field
from rest_framework.serializers import HyperlinkedModelSerializer
from tasks.models import Task


class TaskSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id', 'url', 'task_name', 'is_completed', 
            'has_reminder', 'reminder_timestamp'
        ]
