from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import AccountSerializer,AccountGetSerializer,StudentSerializer,AcademicsSerializer,SportsSerializer,ActivitySerializer
from .models import SignUp
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import settings
import json,nexmo,random
class AuthRegister(APIView):
    """
    Register a new user.
    """
    serializer_class = AccountSerializer
    permission_classes = (AllowAny,)


    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Profile(APIView):
    serializer_class = AccountGetSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self, username):
        try:
            return User.objects.get(username=username)
        except Account.DoesNotExist:
            raise Http404

    def get(self,request,username,format=None):
        account = self.get_object(username)
        serializer=self.serializer_class(account)
        return Response(serializer.data)

class StudentRegister(APIView):
    """
    Save a new student data.
    """
    serializer_class = StudentSerializer
    permission_classes = (AllowAny,)


    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OtpRegister(APIView):

    def post(self,request,format=None):
        length=5
        data=request.database
        print(data)

        a=json.dumps(request.body)
        mobile_number=a['contact']
        client = nexmo.Client(key='66505af0', secret='cltyPLV3jQJQYYwX')
        b=random.sample(range(10**(length-1), 10**length), 1)[0]
        client.send_message({'from': '919473805008', 'to': mobile_number, 'text': b})

        return Response(b, status=status.HTTP_201_CREATED)
