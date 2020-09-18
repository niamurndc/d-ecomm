from django.shortcuts import render
from .models import Product, Category, Brand
# Create your views here.

def index(request):
  category = Category.objects.all()
  brand = Brand.objects.all()
  product = Product.objects.all()
  return render(request, 'index.html', {'products': product, 'cats': category, 'brands': brand})

def show(request, id):
  category = Category.objects.all()
  brand = Brand.objects.all()
  product = Product.objects.get(id=id)
  return render(request, 'product.html', {'product': product, 'cats': category, 'brands': brand})

def shop(request):
  category = Category.objects.all()
  brand = Brand.objects.all()
  product = Product.objects.all()
  return render(request, 'shop.html', {'products': product, 'cats': category, 'brands': brand})

def cart(request):
  return render(request, 'cart.html')

def checkout(request):
  return render(request, 'checkout.html')