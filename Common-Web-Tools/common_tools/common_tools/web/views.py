import random
import time

from django.core.paginator import Paginator
from django.views import generic as views
from django.core.cache import cache
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from common_tools.web.models import Profile


# @cache_page(30)
def show_demo(request):
    if not cache.get('value2'):
        cache.set('value2', random.randint(1, 1024), 30)

    context = {
        'value2': cache.get('value2'),
        'value': 'Hi'
    }
    return render(request, 'demo.html', context)


def show_home_index(request):
    Profile.objects.create(
        name='Ivan Petkov',
        email='ivan123@abv.bg',
    )

    profiles = Profile.objects.all()

    if not cache.get('value2'):
        cache.set('value2', random.randint(1, 1024), 12)

    count = request.session.get('count') or 0
    request.session['count'] = count + 1

    paginator = Paginator(profiles, per_page=5)
    current_page = request.GET.get('page', 1)

    context = {
        'value2': cache.get('value2'),
        'value': random.randint(1, 1024),
        'count': request.session.get('count'),
        'profiles': profiles,
        'profiles_page': paginator.get_page(current_page),
    }

    return render(request, 'index.html', context)


class ProfilesListView(views.ListView):
    model = Profile
    template_name = 'profiles_list.html'
    paginate_by = 5


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
