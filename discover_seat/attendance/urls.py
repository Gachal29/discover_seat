from django.urls import path
from .views import DiscoverSeatView


urlpatterns = [
    path('discover-seat/', DiscoverSeatView.as_view(), name="discover-seat")
]
