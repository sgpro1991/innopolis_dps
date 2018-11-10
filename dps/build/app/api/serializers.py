from api.models import *
from rest_framework import serializers

class AirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Air
        fields = ('t_air', 'datetime', 'Sub_zero')

class StationSerializer(serializers.ModelSerializer):
    data = AirSerializer(many=True, read_only=True)
    class Meta:
        model = Station
        fields = ("id", 'longitude', 'latitude', 'timezone', 'data')
