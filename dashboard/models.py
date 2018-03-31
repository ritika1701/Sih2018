from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.
#class University(models.Model):
  # university_code = models.CharField(max_length=100,primary_key=True)
   #university_name = models.CharField(max_length=1000)

   #def __str__(self):
        #return self.university_code

class School(models.Model):
    schoolcode = models.CharField(max_length=100)
    schoolname = models.CharField(max_length=100)
    #university_code= models.ForeignKey(University,on_delete=models.CASCADE)

    def __str__(self):
        return self.schoolcode


# Registration of school
class SignUp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    schoolcode = models.OneToOneField(School, on_delete=models.CASCADE)
    email = models.EmailField(max_length=70, unique=True)
    contact = models.CharField(max_length=10)
    location = models.TextField(null=True)

    def __str__(self):
        return self.email


# details of student
class Details(models.Model):
    rollno = models.CharField(max_length=100, primary_key=True)
    student_name = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    grade = models.CharField(max_length=100)
    acad_year = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)

    dob = models.DateField(max_length=8)

    teacher_remark = models.TextField(null=True)
    preferred = models.CharField(max_length=100)

    def __str__(self):
        return self.rollno


# academic data and score
class Academics(models.Model):
    eng = models.FloatField(default=0)
    maths = models.FloatField(default=0)
    science = models.FloatField(default=0)
    evs = models.FloaField(default=0)
    sst = models.FloatField(default=0)
    academic_score = models.FloatField(default=0)
    student = models.ForeignKey(Details, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.academic_score)

    def save(self,*args,**kwargs):
        self.academic_score=(self.eng+self.maths+self.science+self.evs+self.sst)/5
        super(Academics,self).save(*args,**kwargs)


# sports data and score
class sports(models.Model):
    sport_name = models.CharField(max_length=100)
    matches = models.IntegerField(default=0)
    semi = models.IntegerField(default=0)
    final = models.IntegerField(default=0)
    won = models.IntegerField(default=0)
    sport_score = models.FloatField(default=0)
    student = models.ForeignKey(Details, on_delete=models.CASCADE)

    def __str__(self):
        return self.sports_played


# activity data and score
class extra_curricular(models.Model):
    activities = models.CharField(max_length=100)
    inter_played = models.IntegerField(default=0)
    inter_won = models.IntegerField(default=0)
    intra_played = models.IntegerField(default=0)
    intra_won = models.IntegerField(default=0)
    student = models.ForeignKey(Details, on_delete=models.CASCADE)

    activity_score = models.FloatField(default=0)

    def __str__(self):
        return self.activities
