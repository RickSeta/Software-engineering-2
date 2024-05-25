from rest_framework import serializers

from ride.serializers.location_serializer import LocationSerializer


class RideSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    available_seats = serializers.IntegerField()
    starting_hour = serializers.DateTimeField()
    starting_point = LocationSerializer()
    destination = LocationSerializer()
    estimated_travel_time = serializers.IntegerField()
    real_travel_time = serializers.IntegerField(required=False)
