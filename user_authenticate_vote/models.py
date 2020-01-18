from django.db import models
from django.contrib.auth.models import User

class Userdetails(models.Model):
# Create your models here.
    adhar_number=models.IntegerField(max_length=12,default=0)
    name=models.CharField(max_length=10,default=None)
    address=models.CharField(max_length=30,default=None)
    father_name=models.CharField(max_length=10,default=None)
    gender=models.ChargerField(default='Male')
    dob=models.DateField(default=None)
    district=models.CharField(max_length=15,default=None)
    taluk=models.CharField(max_length=15,default=None)
    phone_number=models.IntegerField(default=0)
    photo=models.ImageField(default=None)


    

