from django.shortcuts import render, redirect
from .models import Product, Order
from .forms import OrderForm

def home(request):
    return render(request, 'store/home.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def order_create(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()
            return redirect('order_success')
    else:
        form = OrderForm(initial={'product': product})
    return render(request, 'store/order_form.html', {'form': form, 'product': product})

def order_success(request):
    return render(request, 'store/order_success.html')
