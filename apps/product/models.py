from tabnanny import verbose
from django.db import models
from apps.supplier.models import Supplier
from apps.category.models import Category


# Create your models here.
class Product(models.Model):
    
    class ProductStatus(models.TextChoices):
        AVAILABLE = "available", "Available"
        UNAVAILABLE = "unavailable", "Unavailable"


    name = models.CharField(max_length=150)
    sku = models.CharField(max_length=10)
    unit = models.CharField(max_length=10)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.IntegerField()
    status = models.CharField(
        max_length=15,
        choices=ProductStatus.choices,
        default=ProductStatus.AVAILABLE
    )
    supplier = models.ForeignKey(
        Supplier, 
        on_delete=models.CASCADE, 
        related_name="product"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="product"
    )
    image = models.ImageField(upload_to="product")
    expiry_date = models.DateField()
    

    class Meta:
        db_table = "product"
        verbose_name = "product"
        verbose_name_plural = "products"
