from django.shortcuts import render
from django.views.generic import TemplateView


class LoginView(TemplateView):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)