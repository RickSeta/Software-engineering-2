from ride.repositories.location_repository import LocationRepository
from ride.repositories.ride_repository import RideRepository


class CreateRideUseCase:

    def __init__(self, location_repository=None, ride_repository=None):
        self.location_repository = location_repository or LocationRepository()
        self.ride_repository = ride_repository or RideRepository()

    def execute(self, data):
        data['starting_point'] = self.location_repository.get_or_create(
            data['starting_point_address'],
            data['starting_point_latitude'],
            data['starting_point_longitude']
        )
        data['destination'] = self.location_repository.get_or_create(
            data['destination_address'],
            data['destination_latitude'],
            data['destination_longitude']
        )
        data['estimated_travel_time'] = 100
        ride = self.ride_repository.update_or_create(data)
        return ride
