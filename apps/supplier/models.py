import email
from django.db import models

# Create your models here.
class Supplier(models.Model):

    name = models.CharField(blank=False, null=False, max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(blank=False, null=False, unique=True, max_length=50)
    country = models.CharField(max_length=70)
    city = models.CharField(max_length=70)
    address = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="supplier")

    class Meta:
        db_table = "supplier"
        verbose_name = "supplier"
        verbose_name_plural = "suppliers"
    
    def __str__(self) -> str:
        return self.name


    