from django.shortcuts import redirect
from django.views.generic import FormView

from ride.forms.ride_form import RideForm
from ride.models import UserProfile
from ride.use_cases import CreateRideUseCase


class CreateRideView(FormView):
    template_name = 'create_ride.html'
    form_class = RideForm
    use_case = CreateRideUseCase()

    def get_initial(self):
        return {'user': UserProfile.objects.first()}

    def form_valid(self, form):
        ride = self.use_case.execute(form.cleaned_data)
        return redirect('ride:ride_detail', ride.id)
