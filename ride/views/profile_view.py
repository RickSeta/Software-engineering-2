from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from ride.models import UserProfile
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

from ride.forms.user_profile_form import UserProfileForm


User = get_user_model()

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = UserProfile.objects.get(user_id=kwargs.get('user_id'))
        if self.request.user.id == user_profile.user_id:
            context['can_edit'] = True
        context['profile'] = user_profile
        return context
