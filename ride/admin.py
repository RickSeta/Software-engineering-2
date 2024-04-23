from django.contrib import admin
from ride.models import UserProfile, Car, Ride, Location

admin.site.register([
    UserProfile,
    Car,
    Ride,
    Location,
])
