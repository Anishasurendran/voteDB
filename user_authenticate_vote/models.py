from django.db import models
from django.contrib.auth.models import User

class UserDetails(models.Model):
    adhar_number=models.CharField(max_length=12,default=None)
    name=models.CharField(max_length=10,default=None)
    address=models.CharField(max_length=30,default=None)
    father_name=models.CharField(max_length=10,default=None)
    gender=models.CharField(max_length=10,default=None)
    dob=models.DateField(default=None)
    district=models.CharField(max_length=15,default=None)
    taluk=models.CharField(max_length=15,default=None)
    phone_number=models.CharField(max_length=10,default=None)
    photo=models.ImageField(default=None)


    

