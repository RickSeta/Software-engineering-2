from django.test import TestCase
from unittest.mock import Mock

from ride.domain import Car
from ride.factories.car_factory import CarFactory


class CarFactoryTestCase(TestCase):

    def setUp(self):
        self.factory = CarFactory()
        self.model = Mock()

    def test_car_factory(self):
        car = self.factory.create_from_model(self.model)
        self.assertEqual(car.id, self.model.id)
        self.assertEqual(car.model, self.model.model)
        self.assertEqual(car.year, self.model.year)
        self.assertEqual(car.color, self.model.color)
        self.assertEqual(car.plate, self.model.plate)
        self.assertEqual(car.owner_id, self.model.owner.id)
        self.assertIsInstance(car, Car)
