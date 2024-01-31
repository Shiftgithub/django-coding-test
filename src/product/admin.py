from .models import *
from django.contrib import admin


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'sku', 'description']


class VariantAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'active']


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'file_path']


class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ['variant_title', 'get_variant_title', 'get_product_title']

    def get_variant_title(self, obj):
        return obj.variant.title if obj.variant else ''

    get_variant_title.short_description = 'Variant Title'

    def get_product_title(self, obj):
        return obj.product.title if obj.product else ''

    get_product_title.short_description = 'Product Title'


class ProductVariantPriceAdmin(admin.ModelAdmin):
    list_display = ['get_product_variant_one', 'get_product_variant_two', 'get_product_variant_three',
                    'price', 'stock', 'get_product_title']

    def get_product_title(self, obj):
        return obj.product.title if obj.product else ''

    get_product_title.short_description = 'Product Title'

    def get_product_variant_one(self, obj):
        if obj.product_variant_one:
            return obj.product_variant_one.variant_title
        return ''

    get_product_variant_one.short_description = 'Product Variant One'

    def get_product_variant_two(self, obj):
        if obj.product_variant_two:
            return obj.product_variant_two.variant_title
        return ''

    get_product_variant_two.short_description = 'Product Variant Two'

    def get_product_variant_three(self, obj):
        if obj.product_variant_three:
            return obj.product_variant_three.variant_title
        return ''

    get_product_variant_three.short_description = 'Product Variant Three'


admin.site.register(Product, ProductAdmin)
admin.site.register(Variant, VariantAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(ProductVariant, ProductVariantAdmin)
admin.site.register(ProductVariantPrice, ProductVariantPriceAdmin)
