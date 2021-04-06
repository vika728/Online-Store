from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views


urlpatterns = [
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('successful-registration/', views.SuccessfulRegistrationView.as_view(), name='successful-registration'),
    path('activation/', views.ActivationView.as_view(), name='activation-view'),
    path('login/', views.SigninView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('my-profile/<str:email>/', views.ProfileView.as_view(), name='user-profile'),
]