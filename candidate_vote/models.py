from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Location(models.Model):
    cand_location=models.CharField(max_length=30,default=None)
    
class CandidateDetails(models.Model):
    candidate_name=models.CharField(max_length=15,default=None)
    cand_address=models.CharField(max_length=30,default=None)
    cand_gender=models.CharField(max_length=10,default=None)
    cand_district=models.CharField(max_length=10,default=None)
    cand_taluk=models.CharField(max_length=10,default=None)
    cand_phoneno=models.IntegerField(default=0)


class Election(models.Model):
    election_name=models.CharField(max_length=10,default=None)
    election_sdate=models.DateField(default=None)
    election_edate=models.DateField(default=None)
    location=models.ForeignKey(Location,on_delete=models.CASCADE)


class Electioninfo(models.Model):
    election=models.ForeignKey(Election,on_delete=models.CASCADE)
    candidate=models.ForeignKey(CandidateDetails,on_delete=models.CASCADE)

    

class Voting(models.Model):
    elect=models.ForeignKey(Electioninfo,on_delete=models.CASCADE) 
    vote=models.IntegerField(default=0)
    
    
