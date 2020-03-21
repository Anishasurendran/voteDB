from django.db import models
from django.contrib.auth.models import User
from election.models import Location
from .tasks import get_encodings_from_profile_pic
from django.db.models.signals import pre_save

class UserDetails(models.Model):
    user =  models.OneToOneField(User, on_delete=models.CASCADE, default = None)
    adhar_number=models.CharField(max_length=12,default=None)
    name=models.CharField(max_length=10,default=None)
    address=models.CharField(max_length=30,default=None)
    careof=models.CharField(max_length=10,default=None)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob=models.DateField(default=None)
    district=models.CharField(max_length=15,default=None)
    phone_number=models.CharField(max_length=10,default=None)
    photo=models.ImageField(null=True)
    location=models.ForeignKey(Location,on_delete=models.CASCADE,default=None)
    face_encodings = models.BinaryField(null=True)


def save_user(sender, instance, *args, **kwargs):
    instance.face_encodings = get_encodings_from_profile_pic(instance.photo)

pre_save.connect(save_user, sender=UserDetails)
