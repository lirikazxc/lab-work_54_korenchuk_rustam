from django.contrib import admin
from webapp.models.product_model import Product
from webapp.models.category_model import Category


admin.site.register(Product)
admin.site.register(Category)


# Register your models here.
