from .models import Category, Cart, CartItem
from .views import _cart_id

def quantity(request):
    quantity = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.all().filter(cart=cart)
            for cart_item in cart_items:
                quantity += cart_item.quantity
        except Cart.DoesNotExist:
            quantity = 0
    return dict(quantity=quantity)

def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)