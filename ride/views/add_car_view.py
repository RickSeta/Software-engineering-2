from ride.forms.car_form import CarForm
from ride.models import Car, UserProfile
from django.shortcuts import redirect
from django.contrib.auth import get_user_model

User = get_user_model()

def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        user_profile = UserProfile.objects.get(user=request.user)
        if form.is_valid():
            car = form.save(commit=False)
            car.owner = user_profile
            car.save()

    return redirect('ride:profile', request.user.id)
