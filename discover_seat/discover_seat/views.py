from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import AccountSettings


class TopView(LoginRequiredMixin, TemplateView):
    template_name = "top.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        account_settings = AccountSettings.objects.get(user=user)

        context["laboratory"] = account_settings.laboratory

        return context
