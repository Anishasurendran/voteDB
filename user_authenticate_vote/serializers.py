from rest_framework import serializers
from .models import UserDetails

class UserDetailsserializers(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ('adhar_number','name','gender','district','taluk','phone_number','photo')