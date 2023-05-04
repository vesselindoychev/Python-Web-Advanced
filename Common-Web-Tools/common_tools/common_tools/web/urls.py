from django.urls import path

from common_tools.web.views import show_home_index, ProfilesListView, show_demo

urlpatterns = [
    path('', show_home_index, name='show home'),
    path('profiles-list/', ProfilesListView.as_view(), name='profiles list'),
    path('demo/', show_demo, name='show demo'),
]

import common_tools.web.signals