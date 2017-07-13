from django.shortcuts import render, redirect, get_object_or_404
from onlinestoreapp.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from django.views.generic.edit import FormView
from django.views import View


class CartAdd(FormView):
    # form_class = CartAddProductForm

    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        product = get_object_or_404(Product, id=self.kwargs['product_id'])
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product, quantity=cd['quantity'],
                     update_quantity=cd['update'])
        return redirect('cart:CartDetail')


class CartRemove(FormView):
    template_name = 'cart/detail.html'
    form_class = CartAddProductForm

    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        product = get_object_or_404(Product, id=self.kwargs['product_id'])
        cart.remove(product)
        return redirect('cart:CartDetail')


class CartDetail(View):
    template_name = 'cart/detail.html'
    context_object_name = 'cart'

    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        for item in cart:
            item['update_quantity_form'] = CartAddProductForm(
                initial={
                    'quantity': item['quantity'],
                    'update': True
                })
        return render(request, self.template_name, {'cart':cart})