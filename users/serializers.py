from rest_framework.serializers import HyperlinkedModelSerializer
from django.contrib.auth.models import User


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', ]
