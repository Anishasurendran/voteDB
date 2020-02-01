from django.db import models
from django.contrib.auth.models import User
from candidate_vote.models import Location

class UserDetails(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE, default = None)
    adhar_number=models.CharField(max_length=12,default=None)
    name=models.CharField(max_length=10,default=None)
    address=models.CharField(max_length=30,default=None)
    father_name=models.CharField(max_length=10,default=None)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    #gender=models.CharField(max_length=10,default=None)
    dob=models.DateField(default=None)
    district=models.CharField(max_length=15,default=None)
    taluk=models.CharField(max_length=15,default=None)
    phone_number=models.CharField(max_length=10,default=None)
    photo=models.ImageField(default=None)
    location=models.ForeignKey(Location,on_delete=models.CASCADE,default=None)

    

