class UserProfile:

    def __init__(self, attributes):
        self.id = attributes.get('id')
        self.name = attributes.get('name')
        self.username = attributes.get('username')
        self.email = attributes.get('email')
        self.rating = attributes.get('rating')
