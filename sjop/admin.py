from django.contrib import admin

from .models import *



class TabularImagePhoto(admin.TabularInline):

    model = ImageByproduct

    raw_id_fields = ['product']



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name','slug']

    prepopulated_fields = {'slug':('name',)}




@admin.register(Product)
class AdminproductModel(admin.ModelAdmin):

    list_display = ['category','name','price','available','created']

    list_filter = ['created','updated','available']

    prepopulated_fields = {'slug':('name',)}

    list_editable = ['price','available']

    inlines = [TabularImagePhoto]

