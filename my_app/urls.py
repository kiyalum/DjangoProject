from django.urls import path
from .views import test_views, test_views_2

urlpatterns = [
    path('', test_views, name='test_views'),
    path('view2/', test_views_2, name='test_views_2'),
]