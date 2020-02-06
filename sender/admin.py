from django.contrib import admin
from .models import MailForSend

# Register your models here.
@admin.register(MailForSend)
class AdminMailForSend(admin.ModelAdmin):
    pass