from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_POST
from items.models import Item
from .models import Cart, CartItem

@require_POST
def cart_add(request, item_id):
    cart_id = request.session.get('cart_id')

    if cart_id:
        try:
            cart = Cart.objects.get(id = cart_id)
        except Cart.DoesNotExist:
            cart = Cart.objects.create()
    else:
            cart = Cart.objects.create()
            request.session['cart_id'] = cart.id

    item = get_object_or_404(Item, id = item_id)
    cart_item, created = CartItem.objects.get_or_create(cart = cart, item = item)

    if not created:
        cart_item.quantity += 1

    cart_item.save()

    response_data = {
        'success': True,
        'message': f'Added {item.title} to cart'
    }

    return JsonResponse(response_data)

def cart_details(request):
    cart_id = request.session.get('cart_id')
    cart = None

    if cart_id:
        cart = get_object_or_404(Cart, id = cart_id)

    if not cart or not cart.items.exists():
        cart = None

    return render(request, 'cart/detail', {'cart': cart})


def cart_remove(request, item_id):
    cart_id = request.session.get('cart_id')
    cart = get_object_or_404(Cart, id=cart_id)
    item = get_object_or_404(CartItem, id=item_id, cart=cart)
    item.delete()
    
    return redirect("cart:cart_detail")
