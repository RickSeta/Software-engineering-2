from django.shortcuts import redirect
from django.views.generic import FormView
from ride.forms.ride_form import RideForm
from ride.models import UserProfile
from ride.use_cases import CreateRideUseCase
from django.contrib.auth.mixins import LoginRequiredMixin
from ride.mixins.google_maps_api_mixin import GoogleMapsAPIMixin


class CreateRideView(LoginRequiredMixin, GoogleMapsAPIMixin, FormView):
    template_name = 'create_ride.html'
    form_class = RideForm
    use_case = CreateRideUseCase()

    def get_initial(self):
        return {'user': UserProfile.objects.get(user=self.request.user)}

    def form_valid(self, form):
        ride = self.use_case.execute(form.cleaned_data)
        return redirect('ride:ride_detail', ride.id)
