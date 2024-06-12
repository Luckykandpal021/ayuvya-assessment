from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_all_inventory, name='view_all_inventory'),
    path('add_inventory/', views.add_product, name='add_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'), 
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'), 
    path('inventory_stock_details/<int:product_id>/',views.inventory_stock_details,name='inventory_stock_name'),
    path('inventory_order_details/<int:product_id>/', views.inventory_order_details, name='inventory_order_details'),
    path('inventory_stock_transfers/<int:product_id>/', views.inventory_stock_transfer, name='inventory_stock_transfer'),
]
