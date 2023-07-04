from django.contrib import admin
from .models import Category, Item

# Customize the Django Amdinistration Header
admin.site.site_header = "Bookle Admin"

# Customize the admin site and putting anme, price, is_sold on the admin page
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_sold', 'created_by', 'created_at')
    # You can add a filter panel to the side of admin page
    list_filter = ('category',)
    # You can specify which fields you want to have links, by default it is name
    list_display_links = ('name',)
    # You can add a search field
    search_fields = ('name',)

# Register your models here.

admin.site.register(Category)
admin.site.register(Item, ItemAdmin)