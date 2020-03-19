from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from user_authenticate_vote.models import UserDetails
from .models import CandidateDetails,Election,Voting,Location, Electioninfo, UserVoting
from .serializers import CandidateDetailsSerializer,ElectionSerializer,Votingserializer,Locationserializer, ElectionCandidateSerializer



class CandidateDetailsList(generics.ListCreateAPIView):
    queryset = CandidateDetails.objects.all()
    serializer_class = CandidateDetailsSerializer
    #permission_classes = [IsAdminUser]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = CandidateDetailsSerializer(queryset, many=True)
        return Response(serializer.data)

class CandidateDetailsUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = CandidateDetails.objects.all()
    serializer_class = CandidateDetailsSerializer


class ElectionCandidateList(generics.ListAPIView):
    queryset =  Electioninfo.objects.all()
    serializer_class = ElectionCandidateSerializer

    def list(self, request, id):
        queryset =  Electioninfo.objects.filter(election = id)
        serializer = ElectionCandidateSerializer(queryset, many = True)
        return Response(serializer.data)


class ElectionList(generics.ListCreateAPIView):
    queryset = Election.objects.all()
    serializer_class = ElectionSerializer
    #permission_classes = [IsAdminUser]

    def list(self, request):
        user = request.user
        userDetails =  UserDetails.objects.filter(user =  user)
        print(userDetails[0].id)
        queryset = Election.objects.filter(location =  userDetails[0].location)
        serializer = ElectionSerializer(queryset, many=True)
        return Response(serializer.data)

class VotingCreate(generics.CreateAPIView):
    queryset = Voting.objects.all()
    serializer_class = Votingserializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        print(request.user)
        electionId =  request.data['election']
        userVoting = UserVoting.objects.filter(election =  electionId )

        return super().post(request, *args, **kwargs)
