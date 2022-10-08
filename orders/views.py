
from django.shortcuts import render

from django.shortcuts import redirect
from shipping_addresses.models import ShippingAddress



from .utils import destroy_order
from django.contrib import messages
from .utils import get_or_create_order
from carts.utils import get_or_create_cart #esta se encuentra en la carpeta utils de carts

from carts.utils import destroy_cart
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.db.models.query import EmptyQuerySet
 # Create your views here.
 
class OrderListView(ListView):
    login_url = 'login'
    template_name = 'orders/orders.html'

    def get_queryset(self):
        return self.request.user.orders_completed()



# vista de nuestra pagina de order
def order(request):
    cart = get_or_create_cart(request)
    order = get_or_create_order(cart, request)
    
    if not cart.has_products(): #si el carrito de compras no posee productos
        return redirect('carts:cart') #redireccionar a carrito

    return render(request, 'orders/order.html', {
        'cart': cart, #para que salga la imagen en el template de orders
        'order': order, #para ver el precio del total del envio
    })

@login_required(login_url='login')
def address(request):
    cart = get_or_create_cart(request)
    order = get_or_create_order(cart, request)
    
    shipping_address = order.get_or_set_shipping_address()

    return render(request, 'orders/address.html',{
        'cart': cart,
        'order': order,
        'shipping_address': shipping_address,
    })

@login_required(login_url='login') #solo para usuarios autenticados
def select_address(request):
    shipping_addresses = request.user.shipping_address_set.all()
    return render(request, 'orders/select_address.html', {
        'shipping_addresses': shipping_addresses
    })

@login_required(login_url='login') #solo para usuarios autenticados
def check_address(request, pk):
    cart = get_or_create_cart(request)
    order = get_or_create_order(cart, request)

    shipping_address = get_object_or_404(ShippingAddress, pk=pk)

    if request.user.id != shipping_address.user_id:
        return redirect('carts:cart')

    order.update_shipping_address(shipping_address)

    return redirect('orders:address')


@login_required(login_url='login')
def confirm(request):
    cart = get_or_create_cart(request)
    order = get_or_create_order(cart,request)

    shipping_address = order.shipping_address
    if shipping_address is None:
        return  redirect('orders:address')

    return render(request, 'orders/confirm.html',{
        'cart': cart,
        'order': order,
        'shipping_address': shipping_address
    })
    

@login_required(login_url='login')
def cancel(request):
    cart = get_or_create_cart(request)
    order = get_or_create_order(cart, request)

    if request.user.id != order.user_id:
        return redirect('carts:cart')
    
    order.cancel() # las ordenes y el carrito se destruyen 

    destroy_cart(request)
    destroy_order(request)

    messages.error(request, 'Pedido Cancelado')
    return redirect('index')

@login_required(login_url='login')
def complete(request):
    cart = get_or_create_cart(request)
    order = get_or_create_order(cart, request)

    if request.user.id != order.user_id:
        return redirect('carts:cart')
    
    order.complete()

    destroy_cart(request)
    destroy_order(request)

    messages.error(request, '(Compra Realizada) El pedido esta en camino 🚀')
    return redirect('index')