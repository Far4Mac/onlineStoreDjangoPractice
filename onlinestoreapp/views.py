from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Category, Product
from cart.forms import CartAddProductForm


# all available products
class Products(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'store/product/list.html'
    paginate_by = 10

    # def get_queryset(self):
    #     return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Products, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context



class Products_in_category(Products):
    # def get_queryset(self, category_slug):
    #     category = get_object_or_404(Category, slug=category_slug)
    #     return super(Products_in_category, self).get_products().exclude(category__ne=category)

    def get_context_data(self, **kwargs):
        context = super(Products_in_category, self).get_context_data(**kwargs)
        context['category'] = get_object_or_404(Category, slug=self.kwargs['category_slug'])# Category.objects.get(slug=kwargs['category_slug'])
        context['categories'] = Category.objects.all()
        context['products'] = Product.objects.filter(category=context['category'])
        return context


class ProductDetail(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'store/product/detail.html'
    queryset = Product.objects.all()

    def get_object(self):
        return super(ProductDetail, self).get_object()

    def get_context_data(self, **kwargs):
        cart_product_form = CartAddProductForm()
        context = super(ProductDetail, self).get_context_data()
        context['cart_product_form'] = cart_product_form
        return context