from django.views.generic import RedirectView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('ride:search_ride')
