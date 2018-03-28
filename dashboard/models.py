from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class School(models.Model):
    school_code=models.CharField(max_length=100)
    schoolname=models.CharField(max_length=100)
    def __str__(self):
        return self.school_code

class SignUp(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    school_code=models.OneToOneField(School,on_delete=models.CASCADE)
    Principal =models.CharField(max_length=100)
    email= models.EmailField(max_length=70, unique= True)
    contact=models.CharField(max_length=10)

    def __str__(self):
        return self.Principal


class Details(models.Model):
    st_code = models.IntegerField(max_length=100,default=0,primary_key=True)
    name = models.CharField(max_length=100)
    college = models.CharField(max_length=1000)
    email = models.EmailField(max_length=70, unique= True)

    def __str__(self):
        return "{}".format(self.college)

class Academics(models.Model):
    english= models.IntegerField(max_length=10,default=0)
    maths= models.IntegerField(max_length=10,default=0)
    science= models.IntegerField(max_length=10,default=0)
    evs= models.IntegerField(max_length=10,default=0)
    sst= models.IntegerField(max_length=10,default=0)
    student = models.ForeignKey(Details,on_delete=models.CASCADE)


class sports(models.Model):
    sports_played =models.CharField(max_length=100)
    matches =models.IntegerField(max_length=1000,default=0)
    semi =models.IntegerField(max_length=1000,default=0)
    final =models.IntegerField(max_length=1000,default=0)
    won=models.IntegerField(max_length=1000,default=0)
    student = models.ForeignKey(Details,on_delete=models.CASCADE)


    def __str__(self):
        return self.sports_played

class extra_curricular(models.Model):
    ativities =models.CharField(max_length=100)
    total =models.IntegerField(max_length=1000,default=0)
    won =models.IntegerField(max_length=1000,default=0)
    student = models.ForeignKey(Details,on_delete=models.CASCADE)


    def __str__(self):
        return self.activities
