from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Location(models.Model):
    location=models.CharField(max_length=30,default=None)
    
class CandidateDetails(models.Model):
    candidate_name=models.CharField(max_length=45,default=None)
    cand_address=models.CharField(max_length=30,default=None)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default='Male')
    cand_district=models.CharField(max_length=10,default=None)
    cand_taluk=models.CharField(max_length=10,default=None)
    cand_phoneno=models.CharField(max_length=10,default=0)


class Election(models.Model):
    election_name=models.CharField(max_length=10,default=None)
    election_sdate=models.DateField(default=None)
    election_edate=models.DateField(default=None)
    location=models.ForeignKey(Location,on_delete=models.CASCADE,default=None)


class Electioninfo(models.Model):
    election=models.ForeignKey(Election,on_delete=models.CASCADE)
    candidate=models.ForeignKey(CandidateDetails,on_delete=models.CASCADE)

class Voting(models.Model):
    election=models.ForeignKey(Electioninfo,on_delete=models.CASCADE) 
    vote=models.IntegerField(default=0)
    
class UserVoting(models.Model):
    election=models.ForeignKey(Electioninfo,on_delete=models.CASCADE) 
    user =  models.OneToOneField(User, on_delete=models.CASCADE, default = None)
