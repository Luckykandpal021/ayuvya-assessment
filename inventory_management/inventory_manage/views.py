from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Stock, Order, StockTransfer
from .forms import ProductForm,ProductImageForm, StockForm, OrderForm
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


# added new views for updating and deleting inventory_order_details and inventory_stock_transfers

def delete_inventory_stock_details(request, stock_id):
    require_stock_data = get_object_or_404(Stock, id=stock_id)
    require_stock_data.delete()
    return redirect('view_all_inventory')

def edit_stock_details(request,stock_id):
    require_stock_data=get_object_or_404(Stock,id=stock_id)
    if request.method == 'POST':
        form=StockForm(request.POST, instance=require_stock_data)
        if form.is_valid():
            form.save()
            return redirect('inventory_stock_name',product_id=require_stock_data.product.pk)
    else:
        form=StockForm(instance=require_stock_data)    
    
    return render(request, 'templates_views/edit_stock_details.html',{'form':form})


def edit_order_details(request,order_id):
    require_order_details=get_object_or_404(Order,id=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=require_order_details)
        form.save()
        return redirect('inventory_order_details',product_id=require_order_details.product.pk)
    
    else:
        form = OrderForm(instance=require_order_details)

    return render(request, 'templates_views/edit_order_details.html',{'form':form})


def delete_order_details(request,order_id):
    require_order_details=get_object_or_404(Order,id=order_id)
    require_order_details.delete()
    return redirect('view_all_inventory')


