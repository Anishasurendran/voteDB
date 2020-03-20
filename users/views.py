from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import authentication, permissions, parsers
from authy.api import AuthyApiClient
from rest_framework.views import APIView
from django.conf import settings

from .models import UserDetails
from .serializers import UserDetailsserializers, AadharVerifySerializers, PhoneVerifySerializers, PhotoVerifySerializer



authy_api = AuthyApiClient(settings.ACCOUNT_SECURITY_API_KEY)

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


class VerifyAadhar(APIView):
    """
    User aadhar verification

    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        
        verifySerializers =  AadharVerifySerializers(data = request.POST)
        if not verifySerializers.is_valid():
            return Response(verifySerializers.errors, 400)
        else:
            verifySerializers.save()
            authy_api.phones.verification_start(
                verifySerializers.data['phone'],
                '91',
                via='sms'
            )
            
            return Response(verifySerializers.data,200)

class PhoneVerification(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def post(self, request, id, format=None):
        phoneSerializer =  PhoneVerifySerializers(data = request.POST)
        if not phoneSerializer.is_valid():
            return Response(phoneSerializer.errors, 400)
        else:
            phoneSerializer.save()
            userDetails =  UserDetails.objects.get(pk=id)
            verification = authy_api.phones.verification_check(
                userDetails.phone_number,
                '91',
                phoneSerializer.data['otp']
            )
            if verification.ok():
                return Response({
                    "success": True,
                },200)
            else:
                for error_msg in verification.errors().values():
                    print(error_msg)
                return Response({
                    "success": False,
                },400)


class PhotoVerification(APIView):


    parser_class = (parsers.FileUploadParser,)
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]
    
    def post(self, request, id, format=None):
        print(request.POST)
        photoSerializer =  PhotoVerifySerializer(data = request.data)
        if not photoSerializer.is_valid():
            return Response(photoSerializer.errors, 400)
        else:
            photoSerializer.save(user=id)
            return Response(photoSerializer.data)
        image = photoSerializer.data['image']
    
