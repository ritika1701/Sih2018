from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import SignUp,Details,Academics,sports,extra_curricular
from django.contrib.auth.hashers import make_password
import random
import nexmo

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




class AcademicsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Academics
        fields = (
            'eng', 'maths', 'science', 'evs', 'sst')

class SportsSerializer(serializers.ModelSerializer):

    class Meta:
        model = sports
        fields = (
            'sport_name', 'matches', 'semi', 'final', 'won')

class ActivitySerializer(serializers.ModelSerializer):


    class Meta:
        model=extra_curricular
        fields=(
            'activities','inter_played','inter_won','intra_played','intra_won')

class StudentSerializer(serializers.ModelSerializer):

    academics=AcademicsSerializer()
    sports=SportsSerializer(many=True)
    extra_curricular=ActivitySerializer(many=True)

    class Meta:
        model = Details
        fields='__all__'

    def create(self,validated_data):

        marks=validated_data.pop('academics')
        sportinfo=validated_data.pop('sports')
        act=validated_data.pop('extra_curricular')
        student_name=validated_data['student_name']
        validated_data['rollno']=validated_data['rollno']+validated_data['school'].schoolcode
        school=validated_data['school']
        acad_year=validated_data['acad_year']
        grade=validated_data['grade']
        gender=validated_data['gender']
        dob=validated_data['dob']

        teacher_remark=validated_data['teacher_remark']
        preferred=validated_data['preferred']
        print(validated_data)

        detail=Details.objects.create(**validated_data)

        stud=Details.objects.get(rollno=validated_data['rollno'])
        eng=marks['eng']
        maths=marks['maths']
        science=marks['science']
        evs=marks['evs']
        sst=marks['sst']

        score=eng+maths+science+evs+sst

        acad=Academics.objects.create(eng=eng,maths=maths,science=science,evs=evs,sst=sst,academic_score=score,student=stud)


        for i in range(0,len(sportinfo)):
            sports.objects.create(sport_name=sportinfo[i]['sport_name'],matches=sportinfo[i]['matches'],semi=sportinfo[i]['semi'],won=sportinfo[i]['won'],final=sportinfo[i]['final'],sport_score=0,student=stud).save()
        for i in range(0,len(act)):
            extra_curricular.objects.create(activities=act[i]['activities'],inter_played=act[i]['inter_played'],inter_won=act[i]['inter_won'],intra_played=act[i]['intra_played'],intra_won=act[i]['intra_won'],student=stud,activity_score=0).save()


        return detail
