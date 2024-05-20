# from django.db import models
# from django.urls import reverse

# class Category(models.Model):
#     name = models.CharField(max_length=200)

#     class Meta:
#         ordering = ['name']
#         indexes = [
#             models.Index(fields=['name']),
#         ]
#         verbose_name = 'category'
#         verbose_name_plural = 'categories'

#     def __str__(self):
#         return self.name



# class Product(models.Model):
#     default_category = Category.objects.get_or_create(name='Default Category')[0]
#     category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, default=default_category)
#     name = models.CharField(max_length=200)
#     image = models.ImageField(upload_to='images/', blank=True)
#     description = models.TextField(blank=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     available = models.BooleanField(default=True)

#     class Meta:
#         ordering = ['name']
#         indexes = [
#             models.Index(fields=['id']),
#             models.Index(fields=['name']),
#         ]

#     def __str__(self):
#         return self.name




from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, default='default_name')
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product:product_list_by_category', args=[self.slug])

class Product(models.Model):
    default_category = Category.objects.get_or_create(name='Default Category')[0]
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, default=default_category)
    name = models.CharField(max_length=100,)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name



# # class PostalShipment(models.Model):
# #     STATUS_CHOICES = [
# #         ('Pending', 'Pending'),
# #         ('In transit', 'In transit'),
# #         ('Out for delivery', 'Out for delivery'),
# #         ('Delivered', 'Delivered'),
# #         ('Failed', 'Failed'),
# #     ]

# #     sender_name = models.CharField(max_length=100)
# #     recipient_name = models.CharField(max_length=100)
# #     sender_address = models.CharField(max_length=200)
# #     recipient_address = models.CharField(max_length=200)
# #     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
# #     # Добавьте другие поля по необходимости