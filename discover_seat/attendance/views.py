from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from attendance.models import SeatPosition


class DiscoverSeatView(LoginRequiredMixin, TemplateView):
    template_name = "attendance/discover_seat.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        
        try:
            context["seat_position"] = SeatPosition.objects.get(user=user)
        except Exception:
            print("test")
            return redirect(reverse("top"))

        return context
