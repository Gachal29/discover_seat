from django.contrib import admin
from django.urls import path, include
from .views import TopView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TopView.as_view(), name="top"),
    path('', include('accounts.urls'))
]
