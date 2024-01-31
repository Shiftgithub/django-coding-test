from django.views import generic
from django.views.generic import ListView, CreateView, UpdateView

from product.models import *
from product.forms import *
from django.shortcuts import render, redirect


class BaseProductView(generic.View):
    form_class = ProductForm
    model = Product
    template_name = 'products/create.html'
    success_url = '/product/create.product'


# class ProductListView(ListView):
#     model = Product
#     template_name = 'products/list.html'
#     context_object_name = 'products'
#     paginate_by = 10  # Number of items per page
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         product_variants = ProductVariantPrice.objects.filter(product__id=1)  # Filter by product_id = 1
#         context['product_variants'] = product_variants
#         return context

def product_list(request):
    products = Product.objects.all()
    product_variant_prices = ProductVariantPrice.objects.all()
    context = {
        'products': products,
        'product_variant_prices': product_variant_prices,
    }
    return render(request, 'products/list.html', context)


class ProductCreateView(BaseProductView, CreateView):
    success_url = '/product/create/'


class ProductEditView(BaseProductView, UpdateView):
    pk_url_kwarg = 'id'
