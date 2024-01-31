from django.views import generic
from django.views.generic import ListView, CreateView, UpdateView

from product.models import *
from product.forms import *


class BaseProductView(generic.View):
    form_class = ProductForm
    model = Product
    template_name = 'products/create.html'
    success_url = '/product/create.product'


class ProductListView(ListView):
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        # Apply filtering logic based on request parameters
        title_filter = self.request.GET.get('title')
        if title_filter:
            queryset = queryset.filter(title__icontains=title_filter)
        # Add more filters as needed
        return queryset

class ProductCreateView(BaseProductView,CreateView):
    success_url = '/product/create/'


class ProductEditView(BaseProductView, UpdateView):
    pk_url_kwarg = 'id'
