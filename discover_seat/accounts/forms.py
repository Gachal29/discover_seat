from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    class Meta:
        fields = ["username", "password"]
