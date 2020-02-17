from rest_framework import serializers
from rest_framework_jwt.utils import api_settings

from .models import UserDetails




class UserDetailsserializers(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ('adhar_number','name','gender','district','taluk','phone_number','photo')


class AadharVerifySerializers(serializers.Serializer):
    aadhar = serializers.CharField(write_only=True)
    phone =  serializers.CharField(read_only = True)
    user =  serializers.IntegerField(read_only = True)

    def validate(self, attrs):
        aadhar = attrs['aadhar']
        userDetails =  UserDetails.objects.filter(adhar_number = aadhar)
        if not userDetails.exists():
            raise serializers.ValidationError("User does not exist")

        return attrs

    def create(self, validated_data):
        aadhar = validated_data['aadhar']
        userDetails =  UserDetails.objects.get(adhar_number = aadhar)

        validated_data['phone'] = userDetails.phone_number
        validated_data['user'] =  userDetails.id
        
        return validated_data

class PhoneVerifySerializers(serializers.Serializer):
    otp = serializers.CharField()

    def create(self, validated_data):
        return validated_data

class PhotoVerifySerializer(serializers.Serializer):
    photo = serializers.ImageField()
    user = serializers.IntegerField(read_only=True)
    token = serializers.CharField(read_only=True)

    def create(self, validated_data):
        id = validated_data['user']
        user = UserDetails.objects.get(pk = id)
        # following are rest jwt settings
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        token = "JWT " + token
        validated_data['token'] = token
        return validated_data
