class Ride:

    def __init__(self, attributes):
        self.id = attributes.get('id')
        self.status = attributes.get('status')
        self.status_display_name = attributes.get('status_display_name')
        self.driver = attributes.get('driver')
        self.car = attributes.get('car')
        self.available_seats = attributes.get('available_seats')
        self.passengers = attributes.get('passengers')
        self.starting_hour = attributes.get('starting_hour')
        self.starting_point = attributes.get('starting_point')
        self.destination = attributes.get('destination')
        self.estimated_travel_time = attributes.get('estimated_travel_time')
        self.real_travel_time = attributes.get('real_travel_time')
