from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from user.forms.profile_form import ProfileForm
from user.models import Profile

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
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
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)  # ← add request.FILES
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=user_profile)

    return render(request, 'user/profile.html', {
        'form': form,
    })
