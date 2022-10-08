from django.contrib import admin

from PQRS.models import Pqrs

@admin.register(Pqrs)
class PqrsAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'request_subject', 'message']
