from django.shortcuts import render

def checkout(request):
    return render(request, 'order/checkout.html')

def order_success(request, order_id):
    return render(request, 'order/order_success.html', {'order_id': order_id})