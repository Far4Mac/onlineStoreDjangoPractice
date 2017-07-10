from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Category, Product


# all available products
class Products(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'product/list.html'
    paginate_by = 10

    def get_queryset(self):
        return Product.objects.all()


class Products_in_category(Products):
    def get_queryset(self, category_slug):
        category = get_object_or_404(Category, slug=category_slug)
        return super(Products_in_category, self).get_products().exclude(category__ne=category)

    def get_context_data(self, **kwargs):
        context = super(Products_in_category, self).get_context_data(**kwargs)
        context['category'] = get_object_or_404(Category, id=self.args[0], slug=self.args[1])
        return context


class ProductDetail(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'product/detail.html'
    queryset = Product.objects.all()

    def get_object(self):
        return super(ProductDetail, self).get_object()