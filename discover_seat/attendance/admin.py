from django.contrib import admin
from attendance.models import Attendance, SeatPosition


admin.site.register(Attendance)
admin.site.register(SeatPosition)
