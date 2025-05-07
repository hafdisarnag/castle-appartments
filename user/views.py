from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProfileForm
from .models import Profile

def profile_view(request):
    return render(request, "user/profile.html", {
        "user": request.user,
        "profile": request.user.profile,
    })


def edit_profile(request):
    profile = request.user.profile
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("profile")
        else:
            messages.error(request, "Failed to update profile.")
    else:
        form = ProfileForm(instance=profile)

    return render(request, "user/edit_profile.html", {
        "form": form
    })
