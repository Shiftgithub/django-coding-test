from django.views import generic
from django.views.generic import ListView, CreateView, UpdateView
from django.core.paginator import Paginator
from product.models import *
from product.forms import *
from django.shortcuts import render


class BaseProductView(generic.View):
    form_class = ProductForm
    model = Product
    template_name = 'products/create.html'
    success_url = '/product/list'



class ProductListView(ListView):
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['variants'] = ProductVariant.objects.all()
        context['product_count'] = Product.objects.all().count()
        context['product_variant_prices'] = ProductVariantPrice.objects.all()

        paginator = Paginator(self.object_list, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        start_range = (page_obj.number - 1) * self.paginate_by + 1
        end_range = min(page_obj.number * self.paginate_by, paginator.count)

        context['page_obj'] = page_obj
        context['start_range'] = start_range
        context['end_range'] = end_range

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.GET.get('title')
        variant = self.request.GET.get('variant')
        price_from = self.request.GET.get('price_from')
        price_to = self.request.GET.get('price_to')
        date = self.request.GET.get('date')

        if title:
            queryset = queryset.filter(title__icontains=title)
        if variant:
            queryset = queryset.filter(variant__variant_title__icontains=variant)
        if price_from:
            queryset = queryset.filter(productvariantprice__price__gte=price_from)
        if price_to:
            queryset = queryset.filter(productvariantprice__price__lte=price_to)
        if date:
            queryset = queryset.filter(created_at__date=date)

        return queryset



def edit_product(request, id):
    products = Product.objects.all(id=id)
    variants = Variant.objects.all()
    product_variant_prices = ProductVariantPrice.objects.all()
    context = {
        'variants': variants,
        'products': products,
        'product_variant_prices': product_variant_prices,
    }
    return render(request, 'products/list.html', context)


class ProductCreateView(BaseProductView, CreateView):
    pass


class ProductEditView(BaseProductView, UpdateView):
    pk_url_kwarg = 'id'
