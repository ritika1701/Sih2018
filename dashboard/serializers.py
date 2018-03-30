from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import SignUp


class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)
    username = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = SignUp
        fields = (
            'username', 'Principal', 'email', 'password', 'confirm_password', 'contact', 'school_code', 'Location')

    def create(self, validated_data):
        a = SignUp.objects.create(Principal=validated_data['Principal'],
                                  email=validated_data['email'],
                                  contact=validated_data['contact'],
                                  school_code=validated_data['school_code'],
                                  user=User.objects.create(username=validated_data['username'],
                                                           password=validated_data['password']),
                                  Location=validated_data['Location'])

        a.save()
        return a
