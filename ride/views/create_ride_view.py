from django.shortcuts import render
from django.views.generic import TemplateView


class CreateRideView(TemplateView):
    template_name = 'create_ride.html'

    def get(self, request):
        return render(request, self.template_name)
