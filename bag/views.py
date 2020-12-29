from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_bag(request):
    """ A view to return the basket contents """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(
                request, f'updated {product.name} quantity to {bag[item_id]}')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(
                request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)

