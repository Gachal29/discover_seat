from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from laboratory.models import Laboratory
from .models import AccountSettings
import re


class Login(LoginView):
    template_name = "registration/login.html"


class CreateAccountView(TemplateView):
    template_name = "registration/register.html"
    
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    
    def post(self, request):
        email = request.POST.get("email")
        if not(re.search("s[0-9]{7}@s.do-johodai.ac.jp", email) or re.search(".+@do-johodai.ac.jp", email)):
            raise ValueError("学内用メールアドレスを使用してください。")

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect(reverse("account-settings", kwargs={"username": username}))

class AccountSettingsView(TemplateView):
    template_name = "registration/account_settings.html"

    def get_context_data(self, username, **kwargs):
        context = super().get_context_data(**kwargs)
        
        try:
            User.objects.get(username=username)
        except Exception:
            return redirect(reverse("top"))

        laboratories = Laboratory.objects.all()
        context["laboratories"] = laboratories

        return context
    
    def post(self, request, username, **kwargs):
        user = User.objects.get(username=username)

        isTeacher = False

        if (re.search(".+@do-johodai.ac.jp", user.email)):
            isTeacher = True

        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")

        user.first_name = first_name
        user.last_name = last_name
        user.save()

        laboratory = Laboratory.objects.get(id=self.request.POST.get("laboratory"))
        
        account_settings = AccountSettings.objects.create(
            user=user,
            laboratory=laboratory,
            isTeacher=isTeacher
        )
        account_settings.save()

        return redirect(reverse("top"))
