from django.db import models
from django.contrib.auth.models import User
from laboratory.models import Laboratory


class AccountSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    laboratory = models.ForeignKey(Laboratory, on_delete=models.CASCADE)
    isTeacher = models.BooleanField(verbose_name="教員", default=False)
