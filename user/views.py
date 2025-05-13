from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from user.forms.profile_form import ProfileForm
from user.models import Profile
from django.contrib import messages
from property.models import Property
from django.http import JsonResponse

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, phone_number='')
            return redirect('login')
        else:
            return render(request, 'user/register.html', {'form': form})
    else:
        return render(request, 'user/register.html', {
            'form': UserCreationForm()
        })

def profile(request):
    user_profile = Profile.objects.filter(user=request.user).first()

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_profile, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
        else:
            messages.error(request, 'Failed to update profile. Please fix the errors below.')
    else:
        form = ProfileForm(instance=user_profile, user=request.user)

    saved_properties = request.user.favorite_properties.all()

    return render(request, 'user/profile.html', {
        'form': form,
        'user': request.user,
        'saved_properties': saved_properties,
    })


def toggle_favorite(request, property_id):
    property = get_object_or_404(Property, id=property_id)

    if request.user in property.favorites.all():
        property.favorites.remove(request.user)
        status = 'removed'
    else:
        property.favorites.add(request.user)
        status = 'added'

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'status': status})

    return redirect('profile')
