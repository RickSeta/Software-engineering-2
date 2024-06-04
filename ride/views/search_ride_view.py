from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse



class SearchRideView(TemplateView):
    template_name = 'search_ride.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        starting_point = request.POST.get('starting_point')
        destination = request.POST.get('destination')
        datetime = request.POST.get('datetime')
        passengers = request.POST.get('passengers')

        context = {
            'starting_point': starting_point,
            'destination': destination,
            'datetime': datetime,
            'passengers': passengers,
            'search_done': True  
        }
        return render(request, self.template_name, context)
