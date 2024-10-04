from django.contrib import admin

from .models import Coupone


@admin.register(Coupone)
class ModelAdminCouopone(admin.ModelAdmin):

    list_display = ['code','valid_from','valid_to','active']

    list_filter = ['valid_from','valid_to','active']

    search_fields = ['code']