from django.urls import path
from .views import (test_views, test_views_2, book_list_fbv, book_detail_fbv, BookListView, BookDetailView,
                    ArticleListView, ArticleDetailView, ArticleCreateView, ArticleDeleteView, ArticleUpdateView)
from django.conf.urls import handler404, handler500


urlpatterns = [
    path('', test_views, name='test_views'),
    path('view2/', test_views_2, name='test_views_2'),
    # path('home/', home_view, name='home_view'),
    # path('articles/', ArticleListView.as_view(), name='article_list'),

    path('fbv/books/', book_list_fbv, name='book_list_fbv'),
    path('fbv/books//', book_detail_fbv, name='book_detail_fbv'),

    path('cbv/books/', BookListView.as_view(), name='BookListView'),
    path('cbv/books//', BookDetailView.as_view(), name='BookDetailView'),

    path('articles/', ArticleListView.as_view(), name='ArticleListView'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='ArticleDetailView'),
    path('articles/create/', ArticleCreateView.as_view(), name='ArticleCreateView'),
    path('articles/update/<int:pk>/', ArticleUpdateView.as_view(), name='ArticleUpdateView'),
    path('articles/delete/<int:pk>/', ArticleDeleteView.as_view(), name='ArticleDeleteView'),
]

handler404 = 'my_app.views.custompage_not_found_view'
handler500 = 'my_app.views.custom_server_error_view'