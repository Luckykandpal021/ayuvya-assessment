from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_description = models.TextField(blank=True, null=True)
    product_original_price=models.FloatField(blank=True,null=True)
    product_discounted_price=models.FloatField(blank=True,null=True)


    def __str__(self):
        return self.product_name

class ProductImage(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE,related_name='images')
    image=models.ImageField(upload_to='product_image/')

    def __str__(self):
        return f"Image For {self.product.product_name}"

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product.product_name} - {self.quantity}"

class Order(models.Model):
    ORDER_SOURCE_CHOICES = [
        ('website', 'Website'),
        ('amazon', 'Amazon'),
        ('flipkart', 'Flipkart'),
        ('myntra', 'Myntra'),
        ('ayuvya', 'Ayuvya'),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_source = models.CharField(max_length=10, choices=ORDER_SOURCE_CHOICES)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.product.product_name}"

class StockTransfer(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    source = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    transfer_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transfer #{self.id} - {self.product.product_name} from {self.source} to {self.destination}"
