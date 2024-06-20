from ride.models import Location
from ride.factories import LocationFactory


class LocationRepository:

    def __init__(self, factory=None):
        self.model = Location
        self.factory = factory or LocationFactory()

    def get_or_create(self, address, latitude, longitude):
        location, created = self.model.objects.get_or_create(
            address=address,
            latitude=latitude,
            longitude=longitude
        )
        return self.factory.create_from_model(location)
