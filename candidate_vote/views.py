from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
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
    serializer = CandidateDetailsserializer(queryset,many=True)


class ElectionList(generics.ListCreateAPIView):
    queryset = Election.objects.all()
    serializer_class = Electionserializer(queryset,many=True)
    #permission_classes = [IsAdminUser]

    def list(self, request):
        user = request.user
        queryset = Election.objects.filter(location =  user.location)
        serializer = Electionserializer(queryset, many=True)
        return Response(serializer.data)

class VotingCreate(generics.CreateAPIView):
    queryset = Voting.objects.all()
    serializer_class = Votingserializer(queryset,many=True)


class VotingUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Voting.objects.all()
    serializer_class=Votingserializer(queryset,many=True)