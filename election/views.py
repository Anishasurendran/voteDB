from django.shortcuts import render
from rest_framework import generics, permissions, views
from rest_framework.response import Response
from django.contrib.auth.models import User
from users.models import UserDetails
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

    def list(self, request, pk):
        queryset =  Electioninfo.objects.filter(election = pk)

        # Check if user has already voted for this election
        userVoting = UserVoting.objects.filter(election = pk)
        if not userVoting.exists():
            serializer = ElectionCandidateSerializer(queryset, many = True)
            return Response(serializer.data)
        else: 
            return Response({"status": False}, 400)


class ElectionList(generics.ListCreateAPIView):
    queryset = Election.objects.all()
    serializer_class = ElectionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):

        user = request.user
        userDetails =  UserDetails.objects.filter(user =  user)
        print(userDetails)
        # Find the location of the user and find if their any election in it
        queryset = Election.objects.filter(location =  userDetails[0].location)
        serializer = ElectionSerializer(queryset, many=True)
        return Response(serializer.data)

class VoteView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, id, format=None):
        electionInfo = Electioninfo.objects.filter(pk=id)
        if electionInfo.exists():
            vote =  Voting.objects.filter(election = electionInfo[0])
            if vote.exists():
                vote[0].vote += 1
                vote[0].save()
                print(electionInfo[0].election.id, request.user.id)
                user =  User.objects.get(pk = request.user.id)
                userVoting = UserVoting(election  = electionInfo[0].election, user =  user)
                userVoting.save()
                
            return Response({'success': True}, 200)   
        else:
            return Response({'success': False}, 400)   

