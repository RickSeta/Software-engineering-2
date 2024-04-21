from django.shortcuts import render
from django.views.generic import TemplateView


class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get(self, request):
        return render(request, self.template_name)
