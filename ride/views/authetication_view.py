from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from ride.forms.auth_form import SignupForm
from ride.models import UserProfile


def authView(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = UserProfile(user=user)
            profile.save()
            messages.success(request, "Criou conta com sucesso!")
            return redirect("ride:login")
    else:
        form = SignupForm()
    return render(request, "registration/signup.html", {"form" : form})
