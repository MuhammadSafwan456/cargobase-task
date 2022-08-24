from pkg_resources import require
from rest_framework import serializers
from .models import FlightInfo


class FlightInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightInfo
        fields = "__all__"


class GetFlightInfoQueryParams(serializers.Serializer):
    airline = serializers.CharField(max_length=10, required=False)
    flight_number = serializers.CharField(max_length=10, required=False)
    date = serializers.DateField(required=False)


class ScrapDataQueryParams(serializers.Serializer):
    airline = serializers.CharField(max_length=10, required=True)
    flight_number = serializers.CharField(max_length=10, required=True)
    date = serializers.DateField(required=True)
