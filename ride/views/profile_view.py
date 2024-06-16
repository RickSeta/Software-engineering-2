from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from ride.models import UserProfile
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

from ride.forms.user_profile_form import UserProfileForm


User = get_user_model()

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get(self, request):
        user = request.user
        user_profile = UserProfile.objects.get(user=user)
        form = UserProfileForm(instance=user_profile)
        
        context = {
            'profile': user_profile,
            'form': form,
        }
        return render(request, self.template_name, context)


    def post(self, request):
        user = User.objects.get(username='henri')
        user_profile = UserProfile.objects.get(user=user)
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        
        if form.is_valid():
            form.save()
        
        context = {
            'profile': user_profile,
            'form': form,
        }
        return render(request, self.template_name, context)
