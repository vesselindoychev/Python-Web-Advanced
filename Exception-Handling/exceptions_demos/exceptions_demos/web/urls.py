from django.urls import path

from exceptions_demos.web.views import HomeView

urlpatterns = (
    path('', HomeView.as_view(), name='index'),
)