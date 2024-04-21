from django.shortcuts import render
from django.views.generic import TemplateView


class SearchRideView(TemplateView):
    template_name = 'search_ride.html'

    def get(self, request):
        return render(request, self.template_name)
