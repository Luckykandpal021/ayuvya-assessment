from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Stock, Order, StockTransfer
from .forms import ProductForm,ProductImageForm
from django.http import HttpResponseNotFound

def view_all_inventory(request):
    products = Product.objects.all()
    for product in products:
        print(f"Product Name: {product.product_name}")
        print(f"Description: {product.product_description}")
        print(f"Original Price: {product.product_original_price}")
        print(f"Discounted Price: {product.product_discounted_price}")
    return render(request, 'templates_views/view_all_inventory.html', {'products': products})


def add_product(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        image_form = ProductImageForm(request.POST, request.FILES)

        if product_form.is_valid() and image_form.is_valid():
            product = product_form.save()
            image = image_form.save(commit=False)
            image.product = product
            image.save()
            return redirect('view_all_inventory') 
    else:
        product_form = ProductForm()
        image_form = ProductImageForm()
    return render(request, 'templates_views/add_inventory.html',{'product_form': product_form, 'image_form': image_form})

def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect('view_all_inventory')

def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('view_all_inventory')
    else:
        form = ProductForm(instance=product)
    return render(request, 'templates_views/edit_product.html', {'form': form})

def inventory_stock_details(request, product_id):
    stocks=Stock.objects.filter(product_id=product_id)
    if not stocks:
        return HttpResponseNotFound('<h1>Not Available that Stock Data</h1>')
    return render(request,'templates_views/inventory_stock_details.html',{'stocks_details':stocks,'product_id':product_id})


def inventory_order_details(request,product_id):
    orders_details = Order.objects.filter(product_id=product_id)
    if not orders_details:
        return HttpResponseNotFound('<h1>Not Found Your Order Details</h1>',product_id)

    return render(request, 'templates_views/inventory_order_details.html', {'orders': orders_details})

def inventory_stock_transfer(request,product_id):
    stock_transfers = StockTransfer.objects.filter(product_id=product_id)
    if not stock_transfers:
        return HttpResponseNotFound('<h1>Not Available that Stock Transfer Data</h1>')
    return render(request, 'templates_views/inventory_stock_transfer.html', {'stock_transfers': stock_transfers})


