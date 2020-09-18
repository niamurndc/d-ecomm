from django.shortcuts import render, redirect
from .models import Cart, Order

# Create your views here.

def cart(request):
  if(request.method == 'POST'):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    payment = request.POST['payment']
    address = request.POST['address']
    product = [request.POST['product']]
    total = request.POST['total']

    order = Order.objects.create(name=name, email=email, phone=phone, payment=payment, address=address, product=product, total=total)
    order.save()
    return redirect('/')
    

