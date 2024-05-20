from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=50, default='default_first_name')
    last_name = models.CharField(max_length=50, default='default_last_name')
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255, default='default_address')
    # другие поля модели
    postal_code = models.CharField(max_length=20, default='default_postal_code')
    city = models.CharField(max_length=100, default='default_sity')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
