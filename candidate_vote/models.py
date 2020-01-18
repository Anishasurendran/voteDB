from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CandidateDetails(models.Model):
    candidate_name=models.CharField(max_length=15,default=None)
    cand_address=models.CharField(max_length=30,default=None)
    cand_gender=models.CharField(max_length=10,default=None)
    cand_district=models.CharField(max_length=10,default=None)
    cand_taluk=models.CharField(max_length=10,default=None)
    cand_phoneno=models.IntegerField(max_length=10,default=None)
    