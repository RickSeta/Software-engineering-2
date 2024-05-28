from ride.domain import UserProfile


class UserProfileFactory:

    def create_from_model(self, model):
        return UserProfile(
            {
                'id': model.id,
                'name': f"{model.user.first_name} {model.user.last_name}",
                'username': model.user.username,
                'email': model.user.email,
                'rating': model.rating,
            }
        )
