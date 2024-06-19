from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from ride.models import UserProfile
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

from ride.forms.user_profile_form import UserProfileForm
from ride.forms.car_form import CarForm


User = get_user_model()

class EditProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'edit_profile.html'

    def get(self, request):
        user_profile = UserProfile.objects.get(user=request.user)
        form = UserProfileForm(instance=user_profile)
        context = {
            'profile': user_profile,
            'form': form,
        }
        return render(request, self.template_name, context)


    def post(self, request):
        user_profile = UserProfile.objects.get(user=request.user)
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

        if form.is_valid():
            form.save()

        return redirect('ride:profile', user_profile.user.id)
    