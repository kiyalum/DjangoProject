from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Author, Book
# from .models import Order, Product, Warehouse, WarehouseStock
from django.db.models import Count, Q, Sum


def test_views(request):
    return HttpResponse("Hello World! 1")


def test_views_2(request):
    return render(request, "my_app/index.html", context={"info": "password"})


def test_views_3(request):
    students = Student.objects.all()
    return render(request, "my_app/index.html", context={"students": students})


def test_views_4(request):
    # authors = Author.objects.annotate(books_count=Count("books"))
    books = Book.objects.filter(
        (Q(price__gt=500) | Q(published_year=2026)) & ~Q(has_discount=True)
    )


def test_views_5(request):
    popular_authors = Author.objects.annotate(
        total_books=Count("books").filter(
            total_books__gt=3
        ).order_by("-total_books")
    )

    books_with_authors = Book.objects.select_related("author").filter(
        Q(price__lt=300) & Q(stock__gt=0)
    )


# def warehouse_views(request):
#     low_stock_items = WarehouseStock.objects.filter(quantity__lt=5).select_related(
#         "warehouse", "product"
#     )
#
#     active_warehouses = Warehouse.objects.filter(is_active=True).filter(
#         Q(city__iexact="Київ") | Q(city__iexact="Львів")
#     )
#
#     product_total_stock = Product.objects.annotate(
#         total_quantity=Sum("warehouselstock__quantity")
#     )
