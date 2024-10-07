from django.contrib import admin

from django.urls import reverse

from django.utils.safestring import mark_safe 

from .models import *


def order_detail(obj):
    url = reverse('order:admin_order_detail', args=[obj.id])
    return mark_safe(f'<a href="{url}">смотреть</a>')


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']





@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','address',
                    'postal_code', 'city', 'paid',
                    'created', 'updated','stripe_id','payment_link',
                    order_detail]
    
    list_filter = ['paid', 'created', 'updated']
    
    inlines = [OrderItemInline]
    