from django.test import TestCase
from django.urls import reverse

from model_bakery import baker
from ride.constants import RideStatus
from ride.models import Ride
from django.contrib.auth.models import User


class FinishRideTestCase(TestCase):

    def setUp(self):
        self.user = baker.make(User)
        baker.make('UserProfile', user=self.user)
        self.client.force_login(self.user)
        self.ride_id = 33
        self.url = reverse('ride:finish_ride', kwargs={'ride_id': self.ride_id})

    def test_finish_ride(self):
        ride = baker.make(Ride, id=self.ride_id, status=RideStatus.IN_PROGRESS.value)
        response = self.client.post(self.url)
        ride.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ride.status, RideStatus.COMPLETED.value)
        self.assertRedirects(response, reverse('ride:my_rides'))
