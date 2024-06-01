from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.latitude}, {self.longitude}"


class Car(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=100)
    plate = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.model} - {self.plate}"


class Ride(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    available_seats = models.IntegerField()
    passengers = models.ManyToManyField(UserProfile, related_name='rides', blank=True)
    starting_hour = models.DateTimeField()
    starting_point = models.ForeignKey(Location, on_delete=models.PROTECT, related_name='rides_as_starting_point')
    destination = models.ForeignKey(Location, on_delete=models.PROTECT, related_name='rides_as_destination')
    estimated_travel_time = models.IntegerField()
    real_travel_time = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.car.model} - {self.starting_hour}"


class RideRequest(models.Model):
    starting_hour = models.DateTimeField()
    starting_point = models.ForeignKey(Location, on_delete=models.PROTECT, related_name='ride_requests_as_starting_point')
    destination = models.ForeignKey(Location, on_delete=models.PROTECT, related_name='ride_requests_as_destination')
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.created_by} - {self.starting_hour}"


class Review(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.ride} - {self.author}"


class Place(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.PROTECT, related_name='places')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
