# from django.db import models
# from client.models import Client
# from delivery.models import Product

# class Order(models.Model):
#     client = models.ForeignKey(Client, related_name='orders', on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     paid = models.BooleanField(default=False)

#     def __str__(self):
#         return f'Order {self.id}'

#     def get_total_cost(self):
#         return sum(item.get_cost() for item in self.items.all())

# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
#     delivery = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     quantity = models.PositiveIntegerField(default=1)

#     def __str__(self):
#         return f'OrderItem {self.id}'

#     def get_cost(self):
#         return self.price * self.quantity

