from django.db import models
# from .models import Student, Product

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
    # price__gt = 100
    # title__icontains = 'python'
    #

# class ProductManager(models.Manager):
#     def get_queryset(self):

