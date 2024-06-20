from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ride.models import Ride
from django.db.models import Q

class MyRidesView(LoginRequiredMixin, TemplateView):
    template_name = 'my_rides.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rides'] = Ride.objects.filter(Q(passengers=self.request.user.userprofile) | Q(car__owner=self.request.user.userprofile)).order_by('starting_hour')
        return context
