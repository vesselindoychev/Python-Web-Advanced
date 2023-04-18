import random

from django.core.cache import cache
from django.shortcuts import render
from django.views.decorators.cache import cache_page


@cache_page(30)
def show_home_index(request):
    if not cache.get('value2'):
        cache.set('value2', random.randint(1, 1024), 30)
    context = {
        'value2': random.randint(1, 1024),
        'value': random.randint(1, 1024),
    }

    return render(request, 'index.html', context)
