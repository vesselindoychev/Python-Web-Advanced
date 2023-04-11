from django.contrib.auth import views as auth_views, get_user_model, login
from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import forms as auth_forms
from django import forms

from auth_demos.auth_app.models import Profile

UserModel = get_user_model()


class HomeView(views.TemplateView):
    template_name = 'base.html'


class DashboardView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = Profile
    template_name = 'dashboard.html'


class UserRegistrationForm(auth_forms.UserCreationForm):
    first_name = forms.CharField(
        max_length=25,
    )

    class Meta:
        model = UserModel
        fields = ('email',)

    def clean_first_name(self):
        return self.cleaned_data['first_name']

    def save(self, commit=True):
        user = super().save(commit=commit)

        # profile = Profile(
        #     **self.cleaned_data,
        #     user=user,
        # )
        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            user=user,
        )

        if commit:
            profile.save()

        return user


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)


class UserRegistrationView(views.CreateView):
    # form_class = auth_forms.UserCreationForm
    form_class = UserRegistrationForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        result = super().form_valid(form)
        profile = Profile(
            first_name=form.cleaned_data['first_name'],
            user=self.object,
        )

        profile.save()
        login(self.request, self.object)
        return result


class UserLoginView(auth_views.LoginView):
    template_name = 'auth/login.html'

    def get_success_url(self):
        next_url = self.request.GET.get('next', None)
        if next_url:
            return next_url
        return reverse_lazy('home')


class UserLogoutView(auth_views.LogoutView):
    def get_next_page(self):
        return reverse_lazy('home')
