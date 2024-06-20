from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ride.models import Ride
from django.db.models import Q
from ride.constants import RideStatus


class MyRidesView(LoginRequiredMixin, TemplateView):
    template_name = 'my_rides.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rides'] = Ride.objects.filter(
            Q(passengers=self.request.user.userprofile) | Q(car__owner=self.request.user.userprofile), status__in=[RideStatus.SCHEDULED.value, RideStatus.IN_PROGRESS.value]
        ).order_by('starting_hour')
        return context
