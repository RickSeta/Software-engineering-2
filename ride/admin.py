from django.contrib import admin
from ride.models import UserProfile, Car, Ride, Location, RideRequest

admin.site.register([
    UserProfile,
    Car,
    Ride,
    RideRequest,
    Location,
])
