from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price']
    list_editable = ['price']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)