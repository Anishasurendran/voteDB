from rest_framework import serializers
from .models import TempData


class TempDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = TempData
        fields = '__all__'
