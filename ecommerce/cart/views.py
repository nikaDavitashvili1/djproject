from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from products.models import Product
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Purchase

def get_cart(request):
    cart = request.session.get('cart', {})
    return cart

def view_cart(request):
    cart = get_cart(request)
    products = []
    total_price = 0

    for product_id, quantity in cart.items():
        product = Product.objects.get(id=int(product_id))
        total_price += product.price * quantity
        products.append({'product': product, 'quantity': quantity})

    return render(request, 'cart/cart.html', {'products': products, 'total_price': total_price})


def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id = str(product_id)

    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1

    request.session['cart'] = cart
    messages.success(request, 'Product added successfully.')

    return redirect('cart:view_cart')

def remove_from_cart(request, product_id):
    cart = get_cart(request)
    product_id = str(product_id)

    if product_id in cart:
        del cart[product_id]
        request.session['cart'] = cart
        messages.success(request, 'Product removed successfully.')
    return redirect('cart:view_cart') # aq mgoni shesasworebelia


@login_required
def checkout(request):
    cart = request.session.get('cart', {})

    if not cart:
        messages.warning(request, 'You have nothing in your cart.')
        return redirect('cart:view_cart')

    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        total_price = product.price * quantity

        Purchase.objects.create(
            user=request.user,
            product=product,
            quantity=quantity,
            total_price=total_price
        )

    request.session['cart'] = {}
    messages.success(request, 'Thank you for your purchase! :)')
    return redirect('cart:my_purchases_history')

@login_required
def my_purchases(request):
    purchases_list = Purchase.objects.filter(user=request.user).order_by('-purchased_at')

    paginator = Paginator(purchases_list, 5)
    page_number = request.GET.get('page')
    purchases = paginator.get_page(page_number)

    return render(request, 'cart/purchase_history.html', {'purchases': purchases})