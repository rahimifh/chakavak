
from django.contrib import admin
from .models import Product,agency,apply,slider

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price','available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
@admin.register(agency)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','city', 'phone']
    list_filter = ['city']
@admin.register(apply)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['full_name','email', 'phone']
@admin.register(slider)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']
