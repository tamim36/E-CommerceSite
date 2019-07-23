from django.shortcuts import render, get_object_or_404
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from listings.models import Listing

from django.db.models import Sum,Count

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
        return render(request, 'orders/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/create.html', {'form': form})


def order_manager(request):
    if request.user.is_staff :
        orders = Order.objects.all()
        orders_item = OrderItem.objects.filter()

        test = OrderItem.objects.values('product__id','product__title').annotate(
            total_quantity=Sum('quantity'),
            total_price=Sum('price')).order_by('-total_price')
        print(test)

        context = {
            'orders_item' : orders_item,
            'orders' : orders,
            'test' : test
        }

        return render(request, 'orders/manager.html', context)
    else:
        return render(request, 'orders/manager_Error.html')


def order_detail(request, order_id):
    if request.user.is_staff :
        orders = get_object_or_404(Order, pk=order_id)

        context = {
            'orders' : orders
        }

        return render(request, 'orders/each_order.html', context)
    else:
        return render(request, 'orders/manager_Error.html')