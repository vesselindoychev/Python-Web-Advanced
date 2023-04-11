from django.urls import path

from auth_demos.auth_app.views import UserRegistrationView, HomeView, UserLoginView, UserLogoutView, DashboardView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('register/', UserRegistrationView.as_view(), name='registration'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]