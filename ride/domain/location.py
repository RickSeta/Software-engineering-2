class Location:

    def __init__(self, attributes={}):
        self.id = attributes.get('id')
        self.address = attributes.get('address')
        self.latitude = attributes.get('latitude')
        self.longitude = attributes.get('longitude')
