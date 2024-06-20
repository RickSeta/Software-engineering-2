from django.views.generic import DetailView

from ride.repositories import RideRepository
from datetime import datetime
from ride.serializers.ride_serializer import RideSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
from ride.mixins.google_maps_api_mixin import GoogleMapsAPIMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from ride.constants import RideStatus
from django.contrib import messages
from ride.models import Ride


class RideView(LoginRequiredMixin, GoogleMapsAPIMixin, DetailView):
    repository = RideRepository()
    template_name = 'ride_detail.html'
    context_object_name = 'ride'
    serializer_class = RideSerializer

    def get_object(self):
        return self.repository.get_by_id(self.kwargs['ride_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_scheduled'] = context['ride'].status == RideStatus.SCHEDULED.value
        context['is_in_progress'] = context['ride'].status == RideStatus.IN_PROGRESS.value
        context['is_driver'] = self.request.user.userprofile.id == context['ride'].driver.id
        is_passenger = False
        for passenger in context['ride'].passengers:
            if passenger.id == self.request.user.userprofile.id:
                is_passenger = True
                break
        context['is_passenger'] = is_passenger
        return context

@login_required
def cancel_ride(request, ride_id):
    try:
        ride = get_object_or_404(Ride, id=ride_id)
        ride.status = RideStatus.CANCELLED.value
        ride.canceled_at = datetime.now()
        ride.save()
    except Exception as e:
        messages.error(request, 'Erro ao cancelar carona: {}'.format(e))
    return redirect('ride:my_rides')

@login_required
def start_ride(request, ride_id):
    try:
        ride = get_object_or_404(Ride, id=ride_id)
        ride.status = RideStatus.IN_PROGRESS.value
        ride.started_at = datetime.now()
        ride.save()
    except Exception as e:
        messages.error(request, 'Erro ao iniciar carona: {}'.format(e))
    return redirect(request.META.get('HTTP_REFERER', 'ride:my_rides'))

@login_required
def finish_ride(request, ride_id):
    try:
        ride = get_object_or_404(Ride, id=ride_id)
        ride.status = RideStatus.COMPLETED.value
        ride.finished_at = datetime.now()
        ride.save()
    except Exception as e:
        messages.error(request, 'Erro ao finalizar carona: {}'.format(e))
    return redirect('ride:my_rides')
