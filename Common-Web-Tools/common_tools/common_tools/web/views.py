import random
import time

from django.views import generic as views
from django.core.cache import cache
from django.shortcuts import render
from django.views.decorators.cache import cache_page


# @cache_page(30)
def show_home_index(request):
    if not cache.get('value2'):
        cache.set('value2', random.randint(1, 1024), 30)

    count = request.session.get('count') or 0
    request.session['count'] = count + 1

    context = {
        'value2': random.randint(1, 1024),
        'value': random.randint(1, 1024),
        'count': request.session.get('count'),
    }

    return render(request, 'index.html', context)


def show_book_details(request, pk):
    last_viewed = request.session.get('last_viewed_books') or []
    last_viewed.append(pk)
    request.session['last_viewed_books'] = last_viewed


class MeasureTimeMixin(views.TemplateView):
    def dispatch(self, request, *args, **kwargs):
        start_time = time.time()
        result = super().dispatch(*args, **kwargs)
        end_time = time.time()
        print(end_time - start_time)
        return result
