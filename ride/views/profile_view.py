from django.shortcuts import render
from django.views.generic import TemplateView
from ride.models import UserProfile
from django.contrib.auth import get_user_model

User = get_user_model()

class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get(self, request):
        user = User.objects.get(username='usuario_mock')

        user_profile = UserProfile.objects.get(user=user)
        
        context = { 'profile': user_profile }
        
        return render(request, self.template_name, context)