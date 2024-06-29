from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', default='default.img')

    def __str__(self):
        return self.name