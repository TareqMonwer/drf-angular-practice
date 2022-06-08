from rest_framework.routers import DefaultRouter
from django.urls import path, include

from tasks.views import TasksViewSet


router = DefaultRouter()
router.register(r'', TasksViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
