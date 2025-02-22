from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializers(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)
    password = serializers.CharField(write_only= True, required= False)
    new_password = serializers.CharField(write_only= True, required= False)
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name','email', 'password', 'new_password']

