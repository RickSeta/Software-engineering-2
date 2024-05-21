from django.shortcuts import render
from django.views.generic import FormView
from ride.forms.ride_form import RideForm
from ride.models import UserProfile




class CreateRideView(FormView):
    template_name = 'create_ride.html'
    form_class = RideForm

    def get_initial(self):
        return {'user': UserProfile.objects.first()}
