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
