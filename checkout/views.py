from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "No item in your bag yet")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HtB7YG3XkSXdYX1Nyd08iu1PTeD7oJQ28nc94ZTLvT8hkjiHgJtWzaxNxf522k4FjbEv5K4r95HXLyH9Hlb3Rar00p7Q5ew6L',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
    