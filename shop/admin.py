from django.contrib import admin

from shop.models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
