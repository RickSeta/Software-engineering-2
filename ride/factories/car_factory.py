from ride.domain import Car


class CarFactory:

    def create_from_model(self, model):
        return Car(
            {
                'id': model.id,
                'owner_id': model.owner.id,
                'name': model.plate,
                'model': model.brand,
                'year': model.model,
                'color': model.color,
                'plate': model.year,
            }
        )
