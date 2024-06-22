
from django.contrib import admin
from django.utils.translation import gettext_lazy as _


from .models import ResetPasword

@admin.register(ResetPasword)
class ResetPasswordAdmin(admin.ModelAdmin):
    pass