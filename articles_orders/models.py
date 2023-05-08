from django.db import models
from django.utils import timezone

class Article(models.Model):
    reference = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=4, decimal_places=2)
    creation_date = models.DateTimeField(default=timezone.now)

class Order(models.Model):
    articles = models.ManyToManyField(Article, through='OrderItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price_with_tax = models.DecimalField(max_digits=10, decimal_places=2)
    creation_date = models.DateTimeField(default=timezone.now)

class OrderItem(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
