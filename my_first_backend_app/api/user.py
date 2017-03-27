from django.conf import settings
from django.contrib.sites import requests
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import AllowAny
from rest_framework_mongoengine.serializers import DocumentSerializer
from rest_framework_mongoengine.viewsets import ModelViewSet

from my_first_backend_app.api.authentication import BasicAuthentication
from my_first_backend_app.models import User

class UserSerializer(DocumentSerializer):

    class Meta:
        model = User
        fields = '__all__'


class UserViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    authentication_classes = (BasicAuthentication,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    class Meta:
        model = User

    def create(self, request, *args, **kwargs):
        response = super(UserViewSet, self).create(request, *args, **kwargs)
        return response
