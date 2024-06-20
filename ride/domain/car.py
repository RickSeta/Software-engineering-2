class Car:

    def __init__(self, data):
        self.id = data.get('id')
        self.owner_id = data.get('owner_id')
        self.model = data.get('model')
        self.year = data.get('year')
        self.color = data.get('color')
        self.plate = data.get('plate')
