from django.views.generic import CreateView, DetailView
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model
from django.views.generic.base import View
from django.urls import reverse_lazy

from apps.account.forms import RegistrationForm, SigninForm

User = get_user_model()


class RegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'account/registration.html'
    success_url = reverse_lazy('successful-registration')


class SuccessfulRegistrationView(View):
    def get(self, request):
        return render(request, 'account/successfull_registration.html')


class ActivationView(View):
    def get(self, request):
        code = request.GET.get('u')
        user = get_object_or_404(User, activation_code=code)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return render(request, 'account/activation.html')


class SigninView(LoginView):
    form_class = SigninForm
    template_name = 'account/login.html'
    success_url = reverse_lazy('index')


class ProfileView(DetailView):
    model = User
    template_name = 'account/profile.html'
    pk_url_kwarg = 'email'


class ForgotPassword():
    pass


class ChangePassword():
    pass