from django.db import models

from django.contrib.auth.models import User


# Create your models here.

class School(models.Model):
    school_code = models.CharField(max_length=100)
    schoolname = models.CharField(max_length=100)

    def __str__(self):
        return self.school_code


# Registration of school
class SignUp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school_code = models.OneToOneField(School, on_delete=models.CASCADE)
    Principal = models.CharField(max_length=100)
    email = models.EmailField(max_length=70, unique=True)
    contact = models.CharField(max_length=10)
    Location = models.TextField(null=True)

    def __str__(self):
        return self.Principal


# details of student
class Details(models.Model):
    st_code = models.IntegerField(default=0, primary_key=True)
    name = models.CharField(max_length=100)
    college = models.CharField(max_length=1000)


    def __str__(self):
        return "{}".format(self.college)


# academic data and score
class Academics(models.Model):
    english = models.IntegerField(default=0)
    maths = models.IntegerField(default=0)
    science = models.IntegerField(default=0)
    evs = models.IntegerField(default=0)
    sst = models.IntegerField(default=0)
    Academic_score = models.IntegerField(default=0)
    student = models.ForeignKey(Details, on_delete=models.CASCADE)


# sports data and score
class sports(models.Model):
    sports_played = models.CharField(max_length=100)
    matches = models.IntegerField(default=0)
    semi = models.IntegerField(default=0)
    final = models.IntegerField(default=0)
    won = models.IntegerField(default=0)
    sport_score = models.IntegerField(default=0)
    student = models.ForeignKey(Details, on_delete=models.CASCADE)

    def __str__(self):
        return self.sports_played


# activity data and score
class extra_curricular(models.Model):
    ativities = models.CharField(max_length=100)
    Inter_played = models.IntegerField(default=0)
    Inter_won = models.IntegerField(default=0)
    Intra_played = models.IntegerField(default=0)
    Intra_won = models.IntegerField(default=0)
    student = models.ForeignKey(Details, on_delete=models.CASCADE)
    activity_score = models.IntegerField(default=0)

    def __str__(self):
        return self.activities
