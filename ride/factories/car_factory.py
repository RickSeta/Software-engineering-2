from ride.domain import Car


class CarFactory:

    def create_from_model(self, model):
        return Car(
            {
                'id': model.id,
                'owner_id': model.owner.id,
                'model': model.model,
                'year': model.year,
                'color': model.color,
                'plate': model.plate,
            }
        )
