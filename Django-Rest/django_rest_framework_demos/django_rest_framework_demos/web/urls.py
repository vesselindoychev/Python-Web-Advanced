from django.urls import path

from django_rest_framework_demos.web.views import IndexView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
)