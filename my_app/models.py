from django.db import models
from .managers import ActiveManager


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Name: {self.name};  Age: {self.age}"


class Product(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    objects = models.Manager()
    active_objects = ActiveManager()


class Author(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    price = models.DecimalField(max_digits=0, default=0)
    stock = models.PositiveIntegerField(default=0)


# class Warehouse(models.Model):
#     name = models.CharField(max_length=50)
#     city = models.CharField(max_length=50)
#     is_active = models.BooleanField(default=True)
#
#
# class Product(models.Model):
#     sku = models.CharField(unique=True)
#     title = models.CharField(max_length=50)
#     base_price = models.DecimalField(max_digits=10)
#
#
# class WarehouseStock(models.Model):
#     warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE,)
#     quantity = models.PositiveIntegerField(default=0)
#     reserved_quantity = models.PositiveIntegerField(default=0)
#
#
# class Order(models.Model):
#     warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=50)
#
#
# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
#     product = models.ForeignKey(Product, on_delete=models.PROTECT)
#     quantity = models.PositiveIntegerField(verbose_name="Quantity")
#     price_at_order = models.DecimalField(max_digits=10)







