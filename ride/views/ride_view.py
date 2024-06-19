from django.views.generic import DetailView

from ride.repositories import RideRepository
from ride.serializers.ride_serializer import RideSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
from ride.mixins.google_maps_api_mixin import GoogleMapsAPIMixin


class RideView(LoginRequiredMixin, GoogleMapsAPIMixin, DetailView):
    repository = RideRepository()
    template_name = 'ride_detail.html'
    context_object_name = 'ride'
    serializer_class = RideSerializer

    def get_object(self):
        return self.repository.get_by_id(self.kwargs['ride_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_driver'] = self.request.user.userprofile.id == context['ride'].driver.id
        is_passenger = False
        for passenger in context['ride'].passengers:
            if passenger.id == self.request.user.userprofile.id:
                is_passenger = True
                break
        context['is_passenger'] = is_passenger
        return context
