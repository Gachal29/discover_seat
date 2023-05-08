from django.db import models
from django.contrib.auth.models import User


class Laboratory(models.Model):
    """研究室
    """

    def create_lab(self, user, name):
        if (not user.email[user.email.find("@"):] == "@do-johodai.ac.jp"):
            raise ValueError("学生は研究室を作成できません。")
        
        lab = Laboratory.objects.create(name=name, admin_user=user)
        lab.save()
        return lab

    name = models.CharField(
        verbose_name="研究室名",
        max_length=100,
    )

    admin_user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = verbose_name_plural = "研究室"

    def __str__(self):
        return self.name