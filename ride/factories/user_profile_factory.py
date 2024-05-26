from ride.domain import UserProfile


class UserProfileFactory:

    def create_from_model(self, model):
        return UserProfile(
            {
                'id': model.id,
                'name': f"{model.first_name} {model.last_name}",
                'username': model.username,
                'email': model.email,
                'rating': model.rating,
            }
        )
