from .serializers import UserSerializers
from rest_framework import viewsets
from django.contrib.auth.models import User


class UserCreationAPI(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers