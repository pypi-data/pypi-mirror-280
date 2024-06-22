from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from utils.models import TimeStampAbstractModel
from utils.utils import generate_code


User = get_user_model()


class ResetPasword(TimeStampAbstractModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='codes',
    )
    is_active = models.BooleanField()
    code = models.IntegerField(
        unique=True,
        blank=True,
        null=True
    )
    data = models.DateField(
        auto_now_add=True,
        auto_created=True,
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        code = generate_code()
        if not self.code:
            self.code = code
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.user.email}---{self.data}"
        
    class Meta:
        db_table = 'codes_res_password'
        managed = True
        verbose_name = 'Код для сброса пароля'
        verbose_name_plural = 'Коды для  сброса пароля'  

