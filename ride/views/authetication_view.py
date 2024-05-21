from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("ride:login")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form" : form})
