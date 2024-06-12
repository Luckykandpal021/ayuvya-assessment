from django.contrib import admin
from .models import Product, Stock, Order, StockTransfer, ProductImage

class ProductImageInline(admin.TabularInline):
    model=ProductImage
    extra=1

class ProductAdmin(admin.ModelAdmin):
    inlines=[ProductImageInline]

admin.site.register(Product, ProductAdmin)
admin.site.register(Stock)
admin.site.register(ProductImage)
admin.site.register(Order)
admin.site.register(StockTransfer)
