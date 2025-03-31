from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    ordering = ('-price',)
    search_fields = ('name',)
    list_filter = ('price',)


admin.site.register(Product, ProductAdmin)