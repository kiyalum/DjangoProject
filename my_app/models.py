from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Name: {self.name}; Age: {self.age}"

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=50)

    def __str__(self):
        return f"Name: {self.name};  Price: {self.price};  Category: {self.category}"
