from django.contrib import admin
from .models import Patient


class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'delivery_date', 'submission_date', 'update_date')


admin.site.register(Patient, PatientAdmin)
