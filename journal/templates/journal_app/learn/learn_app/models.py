from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Kid(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50,unique=True)
    dob=models.DateField()

    def __str__(self):
        return self.name

class Student(models.Model):
    roll_no=models.ForeignKey(Kid,on_delete=models.CASCADE)
    marks=models.IntegerField()

class Employee(models.Model):
    emp_name=models.CharField(max_length=50)
    emp_age=models.IntegerField()
    emp_desig=models.CharField(max_length=50)

    def __str__(self):
        return self.emp_name

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    portfolio=models.URLField(blank=True)
    pic=models.ImageField(upload_to='pics',blank=True)

    def __str__(self):
        return self.user.username
