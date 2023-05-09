from pydoc import describe
from django.db import models

# Create your models here.
class Category(models.Model):

    category_name = models.CharField(blank=False, null=False, max_length=50, unique=True)
    category_code = models.CharField(blank=False, null=False, max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "category"

    def __str__(self) -> str:
        return self.category_name
    
