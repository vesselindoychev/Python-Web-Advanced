from django.urls import path

from common_tools.web.views import show_home_index

urlpatterns = [
    path('', show_home_index, name='show home'),
]

import common_tools.web.signals