from rest_framework import serializers
#from django.contrib.auth.models import 
from .models import CandidateDetails,Election,Electioninfo,Voting,Location

class CandidateDetailsserializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateDetails
        fields = ('candidate_name', 'gender', 'cand_district', 'cand_taluk',)
 
class Electionserializer(serializers.ModelSerializer):
    class Meta:
        model = Election
        fields = "__all__"
    
class Electioninfoserializer(serializers.ModelSerializer):
    class Meta:
        model = Electioninfo
        fields = "__all__"

class Votingserializer(serializers.ModelSerializer):
    class Meta:
        model = Voting
        fields = "__all__"
 
 

class Locationserializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ("__all__")


 
 