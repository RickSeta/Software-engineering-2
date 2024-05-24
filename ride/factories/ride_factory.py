from ride.domain import Ride
from ride.factories import LocationFactory, CarFactory


class RideFactory:

    def __init__(self, location_factory=None, car_factory=None):
        self.location_factory = location_factory or LocationFactory()
        self.car_factory = car_factory or CarFactory()

    def create_from_model(self, model):
        return Ride(
            {
                'id': model.id,
                'car': self.car_factory.create_from_model(model.car),
                'available_seats': model.available_seats,
                # 'passengers': model.passengers,
                'starting_hour': model.starting_hour,
                'starting_point': self.location_factory.create_from_model(model.starting_point),
                'destination': self.location_factory.create_from_model(model.destination),
                'estimated_travel_time': model.estimated_travel_time,
                'real_travel_time': model.real_travel_time
            }
        )
