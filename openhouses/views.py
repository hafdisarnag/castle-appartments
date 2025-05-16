from django.shortcuts import render
from datetime import datetime, timedelta
from property.models import Property
from django.core.paginator import Paginator
from django.http import HttpResponse

def get_paginated_open_houses(page_number, per_page=3):
    now = datetime.now()
    in_two_weeks = now + timedelta(weeks=2)

    queryset = Property.objects.filter(
        open_house_time__gte=now,
        open_house_time__lte=in_two_weeks
    ).order_by('open_house_time')

    paginator = Paginator(queryset, per_page)

    try:
        return paginator.page(page_number)
    except:
        return None

def get_upcoming_open_houses():
    return get_paginated_open_houses(1)

def load_more_openhouses(request):
    page_number = request.GET.get('page')
    page_obj = get_paginated_open_houses(page_number)

    if not page_obj:
        return HttpResponse('')

    return render(request, 'open houses/load_more_openhouses.html', {'open_houses': page_obj})
