from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from .models import Student, Author, Book, Course, Article
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CourseForm, ArticleForm
# from .models import Order, Product, Warehouse, WarehouseStock
from django.db.models import Count, Q, Sum
from mixins import ActionLoggingMixin


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


"""def course_create(request):
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.save()
            form.save_m2m()
            return redirect("course_list")
    else:
        form = CourseForm()
    return render(request, 'my_app/course_form.html', context={"form": form})


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = "my_app/course_form.html"
    success_url = reverse_lazy("course_list")"""


"""def home_view(request):
    articles = Article.objects.all()
    return render(request, "blog/home.html", context={"articles": articles})


class ArticleListView(ListView):
    model = Article
    template_name = "blog/article_list.html"
    context_object_name = "articles"
    paginate_by = 10

    def get_queryset(self):
        return Article.objects.filter(is_published=True)


class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/article_detail.html"
    context_object_name = "article"


def article_detail_fbv(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, "blog/article_detail.html", {"article": article})"""


def book_list_fbv(request):
    books = Book.objects.all().order_by("-published_year")
    return render(request, "my_app/book_list.html", {"books": books})


def book_detail_fbv(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "my_app/book_detail.html", {"book": book})


class BookListView(ListView):
    """List all books, or create a new book."""
    model = Book
    template_name = "my_app/book_list.html"
    context_object_name = "books"
    paginate_by = 5

    def get_queryset(self):
        return Book.objects.all().order_by("-title")


class BookDetailView(DetailView):
    model = Book
    template_name = "my_app/book_detail.html"
    context_object_name = "book"


# class UserArticleListView(LoginRequiredMixin, ListView):
#     model = Article
#     template_name = "my_app/user_article_list.html"
#     context_object_name = "articles"
#
#     login_url = '/accounts/login/'
#
#     def get_queryset(self):
#         return Article.objects.filter(author=self.request.user)


def custompage_not_found_view(request, exception):
    return render(request, "error/404.html", status=404)


def custom_server_error_view(request):
    return render(request, "error/500.html", status=500)


class ArticleListView(ActionLoggingMixin, ListView):
    model = Article
    template_name = "blog/article_list.html"
    context_object_name = "articles"
    ordering = ["-created_at"]


class ArticleDetailView(ActionLoggingMixin, DetailView):
    model = Article
    fields = ['title', 'content']
    template_name = "blog/article_detail.html"


class ArticleCreateView(ActionLoggingMixin, CreateView):
    model = Article
    form_class =  ArticleForm
    template_name = "blog/article_form.html"
    success_url = reverse_lazy("article_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(ActionLoggingMixin, UpdateView):
    model = Article
    fields = ['title', 'content']
    template_name = "blog/article_form.html"

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author


class ArticleDeleteView(ActionLoggingMixin, DeleteView):
    model = Article
    template_name = "blog/article_confirm_delete.html"
    success_url = reverse_lazy("article_list")

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author


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
