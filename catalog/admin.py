from django.contrib import admin

# Register your models here.
from .models import Category
from .models import Product
admin.site.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name_cat")

admin.site.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display = ("id","name_prod", "price", "category")
    list_filter = ("category",)
    search_fields = ("name_prod", "descr_prod",)
