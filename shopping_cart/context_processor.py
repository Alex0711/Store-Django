from .cart import Cart

def cart_value(request):
    cart=Cart(request)
    check=0
    #if request.user.is_authenticated:
    for key, value in request.session['cart'].items():
        check=check+(float(value['price']))
    return {'cart_value':check}