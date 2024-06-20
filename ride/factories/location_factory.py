from ride.domain import Location


class LocationFactory:

    def create_from_model(self, model):
        return Location(
            {
                'id': model.id,
                'address': model.address,
                'latitude': model.latitude,
                'longitude': model.longitude
            }
        )
