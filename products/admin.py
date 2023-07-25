from django.contrib import admin
from .models import Category, Product, Theme

admin.site.register(Category)
admin.site.register(Theme)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["item_name"]}
    list_filter = ('price',)
    search_fields = ['item_name', 'price']
