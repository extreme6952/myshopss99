from django.contrib import admin

from .models import *



class TabularImagePhoto(admin.TabularInline):

    model = ImageByproduct

    raw_id_fields = ['product']



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name','slug']

    prepopulated_fields = {'slug':('name',)}



@admin.register(Rating)
class RatingTabularInline(admin.ModelAdmin):

    list_display = ['product','user','created','active']

    list_filter = ['created','active']

    raw_id_fields = ['product',]




@admin.register(Product)
class AdminproductModel(admin.ModelAdmin):

    list_display = ['name','category','price','available','created']

    list_filter = ['created','updated','available']

    prepopulated_fields = {'slug':('name',)}

    list_editable = ['price','available']

    inlines = [TabularImagePhoto]



@admin.register(MarketShop)
class AdminMarketshopModel(admin.ModelAdmin):

    list_display = ['name','slug',]

    list_filter = ['created',]

    search_fields = ['name']