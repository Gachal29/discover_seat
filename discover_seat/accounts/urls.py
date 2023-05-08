from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import LoginView, CreateAccountView, AccountSettingsView

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('create-account/', CreateAccountView.as_view(), name="create-account"),
    path('account-settings/<str:username>/', AccountSettingsView.as_view(), name="account-settings"),
]
