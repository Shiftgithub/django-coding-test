from .models import *
from django.contrib import admin


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'sku', 'description']


class VariantAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'active']


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'file_path']


class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ['variant_title', 'variant', 'product']


class ProductVariantPriceAdmin(admin.ModelAdmin):
    list_display = ['product_variant_one', 'product_variant_two', 'product_variant_three', 'price', 'stock',
                    'get_product_title']

    def get_product_title(self, obj):
        return obj.product.title if obj.product else ''

    get_product_title.short_description = 'Product Title'


admin.site.register(Product, ProductAdmin)
admin.site.register(Variant, VariantAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(ProductVariant, ProductVariantAdmin)
admin.site.register(ProductVariantPrice, ProductVariantPriceAdmin)
