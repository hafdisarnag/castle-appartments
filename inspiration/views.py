from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import DesignIdea

def inspiration_home(request):
    category = request.GET.get("category")  # tekur ?category=kitchen úr URL
    if category:
        ideas = DesignIdea.objects.filter(category=category)
    else:
        ideas = DesignIdea.objects.all()

    return render(request, 'inspiration/inspiration.html', {
        'ideas': ideas,
        'selected_category': category,
    })