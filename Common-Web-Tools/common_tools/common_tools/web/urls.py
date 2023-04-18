from django.urls import path

from common_tools.web.views import show_home_index, ProfilesListView

urlpatterns = [
    path('', show_home_index, name='show home'),
    path('profiles-list/', ProfilesListView.as_view(), name='profiles list'),
]

import common_tools.web.signals