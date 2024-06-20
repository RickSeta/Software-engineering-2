from django.test import TestCase
from unittest.mock import Mock

from ride.domain import Location
from ride.factories.location_factory import LocationFactory


class LocationFactoryTestCase(TestCase):

    def setUp(self):
        self.factory = LocationFactory()
        self.model = Mock()

    def test_location_factory(self):
        location = self.factory.create_from_model(self.model)
        self.assertEqual(location.id, self.model.id)
        self.assertEqual(location.latitude, self.model.latitude)
        self.assertEqual(location.longitude, self.model.longitude)
        self.assertEqual(location.address, self.model.address)
        self.assertIsInstance(location, Location)
