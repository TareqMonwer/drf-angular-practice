from rest_framework.viewsets import ModelViewSet

from tasks.serializers import TaskSerializer
from tasks.models import Task


class TasksViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
