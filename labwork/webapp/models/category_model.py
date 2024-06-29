from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return f'Category name:{self.name}'