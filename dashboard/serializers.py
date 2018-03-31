from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import SignUp
from django.contrib.auth.hashers import make_password



class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)
    username = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = SignUp
        fields = (
            'username', 'email', 'password', 'confirm_password', 'contact', 'schoolcode', 'location')

    def create(self, validated_data):
        a = SignUp.objects.create(
                                  email=validated_data['email'],
                                  contact=validated_data['contact'],
                                  schoolcode=validated_data['schoolcode'],
                                  user=User.objects.create(username=validated_data['username'],
                                                           password=make_password(validated_data['password'])),
                                  location=validated_data['location'])

        a.save()
        return a

    def validate(self, data):
        '''
        Ensure the passwords are the same
        '''
        if data['password']:
            print ("Here")
            if data['password'] != data['confirm_password']:
                raise serializers.ValidationError(
                    "The passwords have to be the same"
                )
        return data

class AccountGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username','password')
