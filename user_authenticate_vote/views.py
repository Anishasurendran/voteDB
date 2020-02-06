from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import UserDetails
from .serializers import UserDetailsserializers

class UserDetailsList(generics.ListCreateAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsserializers
    #permission_classes = [IsAdminUser]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserDetailsserializers(queryset, many=True)
        return Response(serializer.data)
class UserDetailsUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsserializers



# Create your views here.
