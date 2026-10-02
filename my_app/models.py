from django.db import models
from .managers import ActiveManager
from django.urls import reverse


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
    title = models.CharField(max_length=50, verbose_name="Book Title")
    author = models.CharField(max_length=100, verbose_name="Author")
    description = models.TextField(verbose_name="Description")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Price")
    published_year = models.PositiveIntegerField(verbose_name="Published Year")
    created_at = models.DateTimeField(auto_now_add=True)
    # stock = models.PositiveIntegerField(default=0)
    # author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return f"{self.title} - {self.author}"

    def get_absolute_url(self):
        return reverse("book-detail-cbv", kwargs={"pk": self.pk})


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Course(models.Model):
    LEVEL_CHOICES = [
        ("beginner", "Початковий"),
        ("intermediate", "Серeдній"),
        ("advanced", "Просунутий"),
    ]

    title = models.CharField(max_length=50, verbose_name="Назва")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Slug")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="courses")
    description = models.TextField(verbose_name="Опис")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Ціна")
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default="beginner")
    is_published = models.BooleanField(default=False, verbose_name="Опубліковано")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)
    duration_minutes = models.PositiveIntegerField(default=0)
    is_free = models.BooleanField(default=False)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.order}: {self.title}"


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


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(verbose_name="Content")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Author" ,related_name="articles")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article-detail-cbv", kwargs={"pk": self.pk})


