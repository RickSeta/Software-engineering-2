from django.test import TestCase
from unittest.mock import Mock

from ride.domain import Ride
from ride.factories.ride_factory import RideFactory


class RideFactoryTestCase(TestCase):

    def setUp(self):
        self.factory = RideFactory()
        self.model = Mock()

    def test_create_from_model(self):
        ride = self.factory.create_from_model(self.model)
        ride.status = self.model.status
        ride.status_display_name = self.model.status_display_name
        ride.driver = self.model.driver
        ride.car = self.model.car
        ride.available_seats = self.model.available_seats
        ride.passengers = self.model.passengers
        ride.starting_hour = self.model.starting_hour
        ride.starting_point = self.model.starting_point
        ride.destination = self.model.destination
        ride.estimated_travel_time = self.model.estimated_travel_time
        ride.real_travel_time = self.model.real_travel_time
        self.assertIsInstance(ride, Ride)
