from django.urls import path
from django.views.generic import TemplateView

from product.views.product import *
from product.views.variant import *

app_name = "product"

urlpatterns = [
    # Variants URLs
    path('variants/', VariantView.as_view(), name='variants'),
    path('variant/create', VariantCreateView.as_view(), name='create.variant'),
    path('variant/<int:id>/edit', VariantEditView.as_view(), name='update.variant'),

    # Products URLs
    path('create/', ProductCreateView.as_view(), name='create.product'),
    path('list/', ProductListView.as_view(), name='list.product'),
    path('edit/<int:id>', ProductEditView.as_view(), name='update.product'),

]
