from rest_framework import serializers
#from django.contrib.auth.models import 
from .models import CandidateDetails,Election,Electioninfo,Voting,Location

class CandidateDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateDetails
        fields = ('candidate_name', 'gender', 'cand_district', 'cand_taluk',)
 
class ElectionSerializer(serializers.ModelSerializer):

    count  =  serializers.SerializerMethodField()

    class Meta:
        model = Election
        fields = ('id', 'election_name','election_sdate', 'election_edate','location', 'count',)

    def get_count(self, obj):
        election_info  = Electioninfo.objects.filter(election = obj).count()
        return election_info
    
class ElectionInfoSerializer(serializers.ModelSerializer):
    election = ElectionSerializer()
    candidate = CandidateDetailsSerializer()

    class Meta:
        model = Electioninfo
        fields = ('election,','candidate',)

class ElectionCandidateSerializer(serializers.ModelSerializer):
    candidate = CandidateDetailsSerializer()

    class Meta:
        model = Electioninfo
        fields = ('candidate',)


class Votingserializer(serializers.ModelSerializer):
    class Meta:
        model = Voting
        fields = "__all__"
 
 

class Locationserializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ("__all__")


 
 