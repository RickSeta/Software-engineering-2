from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ride.models import Ride
from django.db.models import Q
from ride.constants import RideStatus


class RidesHistoryView(LoginRequiredMixin, TemplateView):
    template_name = 'rides_history.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rides'] = Ride.objects.filter(Q(passengers=self.request.user.userprofile) | Q(car__owner=self.request.user.userprofile), status__in=[RideStatus.CANCELLED.value, RideStatus.COMPLETED.value]).order_by('-starting_hour')
        return context
