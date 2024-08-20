from django.contrib import admin

# Register your models here.

from unfold.admin import ModelAdmin

from .models import *



class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']





@admin.register(Order)
class OrderAdmin(ModelAdmin):
    list_display = ['id', 'user',
                    'address', 'postal_code', 'city', 'paid',
                     'created', 'updated',]
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
    