from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.


class Location(models.Model):
    location=models.CharField(max_length=30,default=None)
    def __str__(self):
        return self.location
    
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


    def __str__(self):
        return self.candidate_name


class Election(models.Model):
    election_name=models.CharField(max_length=255,default=None)
    election_sdate=models.DateField(default=None)
    election_edate=models.DateField(default=None)
    location=models.ForeignKey(Location,on_delete=models.CASCADE,default=None)


    def __str__(self):
        return self.election_name


class Electioninfo(models.Model):
    election=models.ForeignKey(Election,on_delete=models.CASCADE)
    candidate=models.ForeignKey(CandidateDetails,on_delete=models.CASCADE)

    def __str__(self):
        return self.election.election_name + "--" + self.candidate.candidate_name

class Voting(models.Model):
    election = models.OneToOneField(Electioninfo,on_delete=models.CASCADE) 
    vote=models.IntegerField(default=0)
    
class UserVoting(models.Model):
    election=models.OneToOneField(Election,on_delete=models.CASCADE) 
    user =  models.ForeignKey(User, on_delete=models.CASCADE, default = None)

def save_user(sender, instance, created, *args, **kwargs):
    print(created)
    if created:
        voting = Voting(election = instance, vote = 0)
        voting.save()

post_save.connect(save_user, sender=Electioninfo)
