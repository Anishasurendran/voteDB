from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from user_authenticate_vote.models import UserDetails
from .models import CandidateDetails,Election,Voting,Location
from .serializers import CandidateDetailsserializer,Electionserializer,Votingserializer,Locationserializer



class CandidateDetailsList(generics.ListCreateAPIView):
    queryset = CandidateDetails.objects.all()
    serializer_class = CandidateDetailsserializer
    #permission_classes = [IsAdminUser]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = CandidateDetailsserializer(queryset, many=True)
        return Response(serializer.data)

class CandidateDetailsUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = CandidateDetails.objects.all()
    serializer_class = CandidateDetailsserializer


class ElectionList(generics.ListCreateAPIView):
    queryset = Election.objects.all()
    serializer_class = Electionserializer
    #permission_classes = [IsAdminUser]

    def list(self, request):
        user = request.user
        userDetails =  UserDetails.objects.filter(user =  user)
        queryset = Election.objects.filter(location =  userDetails[0].location)
        print(queryset)
        serializer = Electionserializer(queryset, many=True)
        return Response(serializer.data)

class VotingCreate(generics.CreateAPIView):
    queryset = Voting.objects.all()
    serializer_class = Votingserializer


class VotingUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Voting.objects.all()
    serializer_class=Votingserializer