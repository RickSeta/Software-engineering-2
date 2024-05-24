from ride.models import Ride
from ride.factories import RideFactory


class RideRepository:

    def __init__(self, factory=None):
        self.model = Ride
        self.factory = factory or RideFactory()

    def update_or_create(self, ride_dict):
        model, created = self.model.objects.update_or_create(
            id=ride_dict.get('id'),
            defaults={
                'car_id': ride_dict.get('car').id,
                'available_seats': ride_dict.get('available_seats'),
                'starting_hour': ride_dict.get('starting_hour'),
                'starting_point_id': ride_dict.get('starting_point').id,
                'destination_id': ride_dict.get('destination').id,
                'estimated_travel_time': ride_dict.get('estimated_travel_time'),
            }
        )
        return self.factory.create_from_model(model)
